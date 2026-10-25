import pytest
from unittest.mock import Mock
from Main_App.EmailAuthentication import EmailAuth
@pytest.fixture
def fake_users(monkeypatch):
    
    user = Mock()
    user.check_password.side_effect = lambda value: value == "CorrectPass123!"
    class UserMissing(Exception):
        pass
    user_model = Mock()
    user_model.DoesNotExist = UserMissing
    def find_user(*, email):
        if email == "student@example.com":
            return user
        raise UserMissing()
    user_model.objects.get.side_effect = find_user
    monkeypatch.setattr(
        "Main_App.EmailAuthentication.get_user_model",
        lambda: user_model
    )
    return user, user_model
def test_auth_valid_credentials(fake_users):
    user, user_model = fake_users
    result = EmailAuth().authenticate(
        username="student@example.com",
        password="CorrectPass123!"
    )
    assert result is user
    user_model.objects.get.assert_called_once_with(email="student@example.com")
    user.check_password.assert_called_once_with("CorrectPass123!")
@pytest.mark.parametrize("email,password", [
    ("student@example.com", "WrongPass123!"),
    ("missing@example.com", "CorrectPass123!"),
    ("", "CorrectPass123!"),
    (None, "CorrectPass123!"),
    ("student@example.com", ""),
    ("student@example.com", None),
    ("studentusername", "CorrectPass123!"),
    ("student@example.com", "correctpass123!"),
    ("student@example.com ", "CorrectPass123!"),
], ids=[
    "wrong-password", "unknown-email", "empty-email", "missing-email",
    "empty-password", "missing-password", "username-not-email",
    "password-case-change", "email-trailing-space"
])
def test_auth_invalid_credentials(fake_users, email, password):
    user, _ = fake_users
    result = EmailAuth().authenticate(username=email, password=password)
    assert result is None
    if email != "student@example.com":
        user.check_password.assert_not_called()
