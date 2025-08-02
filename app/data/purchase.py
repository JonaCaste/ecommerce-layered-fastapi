"""
Purchase repository.

This module contains database operations for purchases.
"""

from data.database import get_connection

class PurchaseData:
    def create_purchase(data):
        """
        Create a new purchase record.

        Args:
            data (dict): JSON with keys: idPurchase, idProduct, idUser, quantity, status, total.
        """
        query = """
            INSERT INTO Purchase ( idProduct, idUser, quantity, status, total)
            VALUES (%s, %s, %s, %s, %s)
        """
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (
            data['idProduct'],
            data['idUser'],
            data['quantity'],
            data.get('status'),
            data.get('total')
        ))
        connection.commit()
        cursor.close()
        connection.close()


    def get_purchases_by_user(user_id):
        """
        Retrieve all purchases made by a specific user.

        Args:
            user_id (int): The user's ID.

        Returns:
            list[dict]: List of purchases.
        """
        query = "SELECT * FROM Purchase WHERE idUser = %s"
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, (user_id,))
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result

    def get_purchase_by_id(purchase_id):
        """
        Retrieve purchase by id.

        Args:
            purchase_id (int): The pruchase ID.

        Returns:
            dict: Purchase.
        """
        query = "SELECT * FROM Purchase WHERE idPurchase = %s"
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, (purchase_id,))
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result
