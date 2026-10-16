
import pytest
from Main_App.models import MyUser, Student


@pytest.mark.django_db
def test_student_profile_update(client):

    #create a test student user
    user = MyUser.objects.create_user(
        username="teststudent",
        email="old@example.com",
        password="Testpass123!",
        user_type="3"
    )

    #create student profile
    student = Student.objects.create(
        admin=user,
        std="5",
        medium="Marathi",
        gender="Male",
        address="Old Address"
    )

    #log in the test user
    client.force_login(user)

    #send profile update request
    response = client.post("/s_saveprofile", {
        "student_id": user.id,
        "firstname": "Ali",
        "lastname": "Khan",
        "email": "ali@example.com",
        "address": "New Address",
        "gender": "Male",
        "password": ""
    })

    #reload updated data
    user.refresh_from_db()
    student.refresh_from_db()

    #verify results
    assert response.status_code == 302
    assert response.url == "/studentprofile"
    assert user.first_name == "Ali"
    assert user.last_name == "Khan"
    assert user.email == "ali@example.com"
    assert student.address == "New Address"
    assert student.gender == "Male"


#student password update tests

@pytest.mark.django_db
@pytest.mark.parametrize("new_password, expected_password", [
    (None, "OldPass123!"),
    ("", "OldPass123!"),
    (" ", " "),
    ("NewPass456!", "NewPass456!")
])
def test_student_password_update(client, new_password, expected_password):

    user = MyUser.objects.create_user(
        username="passwordstudent",
        email="student@test.com",
        password="OldPass123!",
        user_type="3"
    )

    Student.objects.create(
        admin=user,
        std="5",
        medium="Marathi",
        gender="Male",
        address="Old Address"
    )

    client.force_login(user)

    data = {
        "student_id": user.id,
        "firstname": "Ali",
        "lastname": "Khan",
        "email": "student@test.com",
        "address": "Old Address",
        "gender": "Male"
    }

    #none means password field is not submitted
    if new_password is not None:
        data["password"] = new_password

    response = client.post("/s_saveprofile", data)

    user.refresh_from_db()

    assert response.status_code == 302
    assert response.url == "/studentprofile"
    assert user.check_password(expected_password)

    #old password should stop working after an update
    if new_password not in (None, ""):
        assert not user.check_password("OldPass123!")



from django.contrib.messages import get_messages


#test 1: Reject non-POST requests
@pytest.mark.django_db
@pytest.mark.parametrize("method", ["get", "put"])
def test_profile_invalid_method(client, method):

    user = MyUser.objects.create_user(
        username="methodstudent",
        password="TestPass123!",
        user_type="3"
    )

    client.force_login(user)

    response = getattr(client, method)("/s_saveprofile")

    assert "Method not Allowed" in response.content.decode()


#test 2: Invalid student IDs
@pytest.mark.django_db
@pytest.mark.parametrize("student_id", [
    "99999999",      # Nonexistent ID
    "abc",           # Invalid ID format
    None             # Missing ID
])
def test_profile_invalid_student_id(client, student_id):

    user = MyUser.objects.create_user(
        username="invalidstudent",
        email="original@test.com",
        password="TestPass123!",
        user_type="3"
    )

    client.force_login(user)

    data = {
        "firstname": "Ali",
        "lastname": "Khan",
        "email": "changed@test.com",
        "address": "New Address",
        "gender": "Male",
        "password": ""
    }

    if student_id is not None:
        data["student_id"] = student_id

    response = client.post("/s_saveprofile", data)

    user.refresh_from_db()

    assert response.status_code == 302
    assert response.url == "/studentprofile"

    #existing user data should remain unchanged
    assert user.email == "original@test.com"

    #verify error message
    messages = [
        str(message)
        for message in get_messages(response.wsgi_request)
    ]

    assert "Failed to update profile" in messages
