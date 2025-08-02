"""
User repository.

This module manages database operations for users.
"""

from typing import Dict
from data.database import get_connection

class UserData:
    def get_user_by_email(email):
        """
        Retrieve a user by email.

        Args:
            email (str): User's email address.

        Returns:
            dict: The user record or None.
        """
        query = "SELECT * FROM User WHERE email = %s"
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result


    def create_user(data):
        """
        Create a new user.

        Args:
            data (dict): JSON with keys: idUser, username, email, password, direction.
        """
        query = "INSERT INTO User ( username, email, password, direction) VALUES (%s, %s, %s, %s)"
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (
            data['username'],
            data['email'],
            data['password'],
            data['direction']
        ))
        connection.commit()
        cursor.close()
        connection.close()

    def get_user_by_username(username: str) -> Dict:
        """
        Retrieve a user by username.

        Args:
            username (str): User's username.

        Returns:
            dict: The user record or None.
        """
        query = "SELECT * FROM User WHERE username = %s"
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result