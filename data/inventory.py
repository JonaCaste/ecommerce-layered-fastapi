"""
Inventory repository.

This module manages inventory-related operations.
"""

from data.database import get_connection

class InventoryData:
    def get_inventory_by_product(product_id):
        """
        Retrieve inventory information for a given product.

        Args:
            product_id (int): Product ID.

        Returns:
            dict: Inventory record or None.
        """
        query = "SELECT * FROM Inventory WHERE idProduct = %s"
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, (product_id,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result


    def update_inventory_quantity(product_id, new_quantity):
        """
        Update the inventory quantity.

        Args:
            product_id (int): The product record ID.
            new_quantity (int): New quantity to set.
        """
        query = "UPDATE Inventory SET quantity = %s WHERE idProduct = %s"
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, (new_quantity, product_id))
        connection.commit()
        cursor.close()
        connection.close()
