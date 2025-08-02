"""
Service layer for user operations.
"""

from typing import Dict
import bcrypt
import jwt
from data.user import UserData
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

class UserBusiness:
    @staticmethod
    def register_user(data: Dict) -> Dict:
        """
        Handles the logic to register a new user.

        :param data: Dictionary containing user information.
        :return: Dictionary with a success message and registered user data.
        :raises ValueError: If validation fails or email already exists.
        """
        required_fields = {
            'username': str,
            'email': str,
            'password': str,
            'direction': str
        }

        # Validate fields and types
        for field, field_type in required_fields.items():
            if field not in data:
                raise ValueError(f"Missing field: {field}")
            if not isinstance(data[field], field_type):
                raise ValueError(f"Invalid type for field '{field}': expected {field_type.__name__}")

        # Check if email is already in use
        existing_user = UserData.get_user_by_email(data['email'])
        if existing_user:
            raise ValueError("Email is already registered")

        # Hash the password
        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        data['password'] = hashed_password.decode('utf-8')

        # Save user to DB
        UserData.create_user(data)

        return {
            "message": "User successfully registered"
        }

    @staticmethod
    def login_user(data: Dict) -> Dict:
        """
        Handles the logic to authenticate a user.

        :param data: Dictionary with username and password.
        :return: Dictionary with a JWT token if authentication succeeds.
        :raises ValueError: If validation fails or authentication fails.
        """
        required_fields = {
            'username': str,
            'password': str
        }

        for field, field_type in required_fields.items():
            if field not in data:
                raise ValueError(f"Missing field: {field}")
            if not isinstance(data[field], field_type):
                raise ValueError(f"Invalid type for field '{field}': expected {field_type.__name__}")

        # Find user by username
        user = UserData.get_user_by_username(data['username'])
        if not user:
            raise ValueError("Invalid username or password")

        # Validate password
        if not bcrypt.checkpw(data['password'].encode('utf-8'), user['password'].encode('utf-8')):
            raise ValueError("Invalid username or password")

        # Generate JWT token
        now = datetime.now(timezone.utc)
        payload = {
            "user_id": user["idUser"],
            "username": user["username"],
            "exp": now + timedelta(hours=2)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

        return {
            "token": token
        }
