"""
Service layer for inventory operations.
"""

from typing import Dict, Optional
from data.inventory import InventoryData

class InventoryService:
    @staticmethod
    def update_inventory(data: Dict) -> Dict:
        """
        Updates the inventory of a product.

        :param data: Dictionary with product ID and quantity.
        :return: Dictionary with update result.
        :raises ValueError: If required fields are missing or invalid.
        """
        product_id = data.get("idProduct")
        new_quantity = data.get("quantity")

        if product_id is None:
            raise ValueError("The field 'idProduct' is required.")
        if not isinstance(product_id, int) or product_id <= 0:
            raise ValueError("The 'idProduct' is not valid.")

        if new_quantity is None:
            raise ValueError("The field 'quantity' is required.")
        if not isinstance(new_quantity, int) or new_quantity < 0:
            raise ValueError("The 'quantity' must be a non-negative integer.")
        
        #@todo if product not exist in db, we must create it
        
        InventoryData.update_inventory_quantity(product_id, new_quantity)
        return data
    
    @staticmethod
    def get_inventory_by_product(product_id: int) -> Optional[Dict]:
        """
        Retrieves the inventory data for a given product.

        ::param product_id: ID of the product to retrieve inventory for.
        :return: Dictionary with inventory data if found, otherwise None.
        :raises ValueError: If product_id is not a positive integer.
        """

        if not isinstance(product_id, int) or product_id <= 0:
            raise ValueError("The 'product_id' is not valid")

        return InventoryData.get_inventory_by_product(product_id)