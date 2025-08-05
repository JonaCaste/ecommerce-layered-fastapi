import pytest
import bcrypt
from unittest.mock import patch
from business.user import UserBusiness


# ---------- Test register_user ----------

def test_register_user_success():
    data = {
        "username": "john",
        "email": "john@example.com",
        "password": "securepass",
        "direction": "123 Main St"
    }

    with patch("data.user.UserData.get_user_by_email", return_value=None), \
         patch("data.user.UserData.create_user") as mock_create:

        result = UserBusiness.register_user(data.copy())
        mock_create.assert_called_once()
        assert result["message"] == "User successfully registered"


def test_register_user_missing_username():
    data = {
        "email": "john@example.com",
        "password": "securepass",
        "direction": "123 Main St"
    }

    with pytest.raises(ValueError, match="Missing field: username"):
        UserBusiness.register_user(data)


def test_register_user_email_already_exists():
    data = {
        "username": "john",
        "email": "john@example.com",
        "password": "securepass",
        "direction": "123 Main St"
    }

    with patch("data.user.UserData.get_user_by_email", return_value={"idUser": 1}):
        with pytest.raises(ValueError, match="Email is already registered"):
            UserBusiness.register_user(data)


def test_register_user_persistence_error():
    data = {
        "username": "john",
        "email": "john@example.com",
        "password": "securepass",
        "direction": "123 Main St"
    }

    with patch("data.user.UserData.get_user_by_email", return_value=None), \
         patch("data.user.UserData.create_user", side_effect=Exception("DB Error")):

        with pytest.raises(Exception, match="DB Error"):
            UserBusiness.register_user(data)


# ---------- Test login_user ----------

def test_login_user_success():
    password = "securepass"
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    user_record = {
        "idUser": 1,
        "username": "john",
        "password": hashed_pw
    }

    data = {
        "username": "john",
        "password": password
    }

    with patch("data.user.UserData.get_user_by_username", return_value=user_record):
        result = UserBusiness.login_user(data)
        assert "token" in result


def test_login_user_missing_username():
    data = {
        "password": "pass123"
    }

    with pytest.raises(ValueError, match="Missing field: username"):
        UserBusiness.login_user(data)


def test_login_user_invalid_username():
    data = {
        "username": "unknown",
        "password": "somepass"
    }

    with patch("data.user.UserData.get_user_by_username", return_value=None):
        with pytest.raises(ValueError, match="Invalid username or password"):
            UserBusiness.login_user(data)


def test_login_user_wrong_password():
    user_record = {
        "idUser": 1,
        "username": "john",
        "password": bcrypt.hashpw("correctpass".encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    }

    data = {
        "username": "john",
        "password": "wrongpass"
    }

    with patch("data.user.UserData.get_user_by_username", return_value=user_record):
        with pytest.raises(ValueError, match="Invalid username or password"):
            UserBusiness.login_user(data)


def test_login_user_persistence_error():
    data = {
        "username": "john",
        "password": "any"
    }

    with patch("data.user.UserData.get_user_by_username", side_effect=Exception("DB Fail")):
        with pytest.raises(Exception, match="DB Fail"):
            UserBusiness.login_user(data)
