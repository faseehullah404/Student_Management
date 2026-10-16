
import pytest
from Main_App.models import MyUser, Student, Result, Notes


@pytest.mark.django_db
@pytest.mark.parametrize("url, model, context_key", [
    ("/s_viewresult/", Result, "results"),
    ("/s_viewnotes/", Notes, "notes")
])
@pytest.mark.parametrize("scenario", [
    "matching",
    "wrong_std",
    "wrong_medium",
    "no_records",
    "multiple_matches"
])
def test_student_content_filtering(
    client, url, model, context_key, scenario
):
    # Create test student
    user = MyUser.objects.create_user(
        username="contentstudent",
        password="TestPass123!",
        user_type="3"
    )

    Student.objects.create(
        admin=user,
        std="5",
        medium="Marathi",
        gender="Male",
        address="Test Address"
    )

    client.force_login(user)

    # Helper: create test result or note
    def create_record(title, std, medium):
        model.objects.create(
            title=title,
            std=std,
            medium=medium,
            created_by="Tester",
            file="example.pdf"
        )

    expected = []

    if scenario == "matching":
        create_record("Correct", "5", "Marathi")
        expected = ["Correct"]

    elif scenario == "wrong_std":
        create_record("Other Class", "6", "Marathi")

    elif scenario == "wrong_medium":
        create_record("Other Medium", "5", "CBSE")

    elif scenario == "multiple_matches":
        create_record("Correct 1", "5", "Marathi")
        create_record("Correct 2", "5", "Marathi")
        create_record("Other Class", "6", "Marathi")
        expected = ["Correct 1", "Correct 2"]

    # Request student page
    response = client.get(url)

    assert response.status_code == 200
    assert response.context is not None

    # Verify filtered records
    actual = sorted(
        item.title for item in response.context[context_key]
    )

    assert actual == sorted(expected)
