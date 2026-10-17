
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from Main_App.models import MyUser, Teacher, Result, Notes


@pytest.fixture
def logged_in_teacher(client, db):
    user = MyUser.objects.create_user(
        username="teacher_content",
        password="TestPass123!",
        user_type="2"
    )

    Teacher.objects.create(
        admin=user,
        gender="Male",
        address="Test Address"
    )

    client.force_login(user)
    return client


@pytest.mark.django_db
@pytest.mark.parametrize(
    "url, model, context_key",
    [
        ("/t_viewresult/", Result, "results"),
        ("/t_viewnotes/", Notes, "notes"),
    ]
)
@pytest.mark.parametrize(
    "scenario",
    [
        "matching",
        "different_std",
        "different_medium",
        "no_records",
        "multiple_records",
    ]
)
def test_teacher_content_display(
    logged_in_teacher, url, model, context_key, scenario
):
    def create_record(title, std, medium):
        uploaded_file = SimpleUploadedFile(
            f"{title.replace(' ', '_')}.pdf",
            b"test file content",
            content_type="application/pdf"
        )

        return model.objects.create(
            title=title,
            std=std,
            medium=medium,
            created_by="TestTeacher",
            file=uploaded_file
        )

    expected = []

    if scenario == "matching":
        create_record("Matching Content", "5", "Marathi")
        expected = ["Matching Content"]

    elif scenario == "different_std":
        create_record("Different Standard", "6", "Marathi")
        expected = ["Different Standard"]

    elif scenario == "different_medium":
        create_record("Different Medium", "5", "CBSE")
        expected = ["Different Medium"]

    elif scenario == "multiple_records":
        create_record("Content One", "5", "Marathi")
        create_record("Content Two", "6", "CBSE")
        expected = ["Content One", "Content Two"]

    response = logged_in_teacher.get(url)

    assert response.status_code == 200
    assert response.context is not None

    actual = sorted(
        item.title for item in response.context[context_key]
    )

    assert actual == sorted(expected)


@pytest.mark.django_db
@pytest.mark.parametrize(
    "url, context_key",
    [
        ("/t_viewresult/", "results"),
        ("/t_viewnotes/", "notes"),
    ]
)
def test_teacher_content_requires_login(client, url, context_key):
    response = client.get(url)

    assert response.status_code == 302
    assert response.url == "/loginpage"
