
import pytest
from django.db.models.signals import post_save
from Main_App.models import MyUser, Teacher, user_create, user_save


@pytest.fixture
def teacher(db):
    post_save.disconnect(user_create, sender=MyUser)
    post_save.disconnect(user_save, sender=MyUser)

    try:
        user = MyUser(
            username="teacher_zohaib",
            user_type="2"
        )
        user.set_password("OldPass123!")
        user.save()

        Teacher.objects.create(
            admin=user,
            gender="Male",
            address="Old Address"
        )
    finally:
        post_save.connect(user_create, sender=MyUser)
        post_save.connect(user_save, sender=MyUser)

    return user


@pytest.fixture
def logged_in_teacher(client, teacher):
    client.force_login(teacher)
    return client


def test_teacher_profile_update_success(logged_in_teacher, teacher):
    response = logged_in_teacher.post("/t_saveprofile", {
        "teacher_id": teacher.id,
        "firstname": "Zohaib",
        "lastname": "Ahmed",
        "email": "zohaib@example.com",
        "gender": "Female",
        "address": "New Address",
        "password": ""
    })

    assert response.status_code == 302
    assert response.url == "/teacherprofile"

    teacher.refresh_from_db()
    teacher_profile = Teacher.objects.get(admin=teacher)

    assert teacher.first_name == "Zohaib"
    assert teacher.last_name == "Ahmed"
    assert teacher.email == "zohaib@example.com"
    assert teacher_profile.gender == "Female"
    assert teacher_profile.address == "New Address"


def test_teacher_profile_update_without_password(
    logged_in_teacher, teacher
):
    old_password = "OldPass123!"

    response = logged_in_teacher.post("/t_saveprofile", {
        "teacher_id": teacher.id,
        "firstname": "Zohaib",
        "lastname": "Ahmed",
        "email": "zohaib@example.com",
        "gender": "Male",
        "address": "Updated Address",
        "password": ""
    })

    teacher.refresh_from_db()

    assert response.status_code == 302
    assert teacher.check_password(old_password)


def test_teacher_profile_update_with_new_password(
    logged_in_teacher, teacher
):
    new_password = "NewPass456!"

    response = logged_in_teacher.post("/t_saveprofile", {
        "teacher_id": teacher.id,
        "firstname": "Zohaib",
        "lastname": "Ahmed",
        "email": "zohaib@example.com",
        "gender": "Male",
        "address": "Updated Address",
        "password": new_password
    })

    teacher.refresh_from_db()

    assert response.status_code == 302
    assert teacher.check_password(new_password)


def test_teacher_profile_update_rejects_get(
    logged_in_teacher
):
    response = logged_in_teacher.get("/t_saveprofile")

    assert response.status_code == 200
    assert b"Method not Allowed" in response.content


def test_teacher_profile_update_requires_login(client):
    response = client.post("/t_saveprofile", {})

    assert response.status_code == 302
    assert response.url == "/loginpage"
