
import pytest
from unittest.mock import patch
from django.conf import settings
from django.contrib import messages
from django.contrib.messages import get_messages
from Main_App.models import MyUser


@pytest.fixture
def user_factory(db):
    def create_user(user_type):
        user = MyUser.objects.create_user(
            username=f"test_user_{user_type}",
            password="Pass123!",
            user_type=str(user_type)
        )
        user.backend = settings.AUTHENTICATION_BACKENDS[0]
        return user

    return create_user


@pytest.mark.django_db
def test_loginpage_loads(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.templates[0].name == "loginpage.html"


@pytest.mark.parametrize(
    "user_type, expected_url",
    [
        ("1", "/adminhome"),
        ("2", "/teacherhome"),
        ("3", "/studenthome")
    ]
)
def test_login_success_redirects_by_user_type(
    client, user_factory, user_type, expected_url
):
    user = user_factory(user_type)

    with patch(
        "Main_App.views.EmailAuth.authenticate",
        return_value=user
    ) as mock_authenticate:
        response = client.post("/loginuser", {
            "email": "test@example.com",
            "password": "Pass123!"
        })

    assert response.status_code == 302
    assert response.url == expected_url
    mock_authenticate.assert_called_once()


def test_login_invalid_credentials(client):
    with patch(
        "Main_App.views.EmailAuth.authenticate",
        return_value=None
    ):
        response = client.post("/loginuser", {
            "email": "wrong@example.com",
            "password": "WrongPass!"
        })

    assert response.status_code == 302
    assert response.url == "/"

    stored_messages = list(get_messages(response.wsgi_request))
    assert any(
        "Invalid login details" in str(message)
        for message in stored_messages
    )


def test_login_rejects_get_request(client):
    response = client.get("/loginuser")

    assert response.status_code == 200
    assert b"Method not allowed" in response.content


def test_login_invalid_user_type(client, user_factory):
    user = user_factory("4")

    with patch(
        "Main_App.views.EmailAuth.authenticate",
        return_value=user
    ):
        response = client.post("/loginuser", {
            "email": "test@example.com",
            "password": "Pass123!"
        })

    assert response.status_code == 200
    assert b"Invalid user type" in response.content


def test_logout_redirects_to_login_page(client, user_factory):
    user = user_factory("2")
    client.force_login(user)

    response = client.get("/logoutuser")

    assert response.status_code == 302
    assert response.url == "/"
    assert "_auth_user_id" not in client.session
