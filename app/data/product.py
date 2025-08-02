"""
Product repository.

This module handles all database interactions related to products.
"""

from data.database import get_connection

class ProductData:
    def get_all_products():
        """
        Retrieve all products from the database.

        Returns:
            list[dict]: A list of products.
        """
        query = "SELECT * FROM Product"
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result


    def get_product_by_id(product_id):
        """
        Retrieve a single product by its ID.

        Args:
            product_id (int): The product's ID.

        Returns:
            dict: The product record or None if not found.
        """
        query = "SELECT * FROM Product WHERE idProduct = %s"
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, (product_id,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result


    def create_product(data):
        """
        Create a new product in the database.

        Args:
            data (dict): JSON object with keys: name, price, description.
        """
        query = "INSERT INTO Product ( name, price, description) VALUES ( %s, %s, %s)"
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, ( data['name'], data['price'], data['description']))
        connection.commit()
        cursor.close()
        connection.close()
