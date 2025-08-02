"""
Service layer for purchase operations.
"""

from typing import Dict
from fastapi import HTTPException
from business.product import ProductBusiness
from data.purchase import PurchaseData

from business.inventory import InventoryService

class PurchaseService:
    @staticmethod
    def purchase_product(data: Dict) -> Dict:
        """
        Processes a purchase request.

        Validates input fields before proceeding.

        Required fields:
        - idProduct: int
        - idUser: int
        - quantity: int

        :param data: Dictionary with product ID, user ID, quantity, status, and total.
        :return: Dictionary with purchase confirmation.

        Raises:
            HTTPException: If any required field is missing or has invalid type/format.
        """

        # Validate required fields and types
        required_fields = {
            'idProduct': int,
            'idUser': int,
            'quantity': int,
        }

        for field, expected_type in required_fields.items():
            if field not in data:
                return {"error": f"'{field}' is required."}
            if not isinstance(data[field], expected_type):
                return {"error": f"'{field}' must be of type {expected_type}."}
            
        #Validate quantity
        if data["quantity"] < 1:
            raise ValueError("The 'quantity' must be a non-negative integer.")

        #Get product info and calculate total
        try:
            product = ProductBusiness.get_product_by_id(data['idProduct'])
        except ValueError as e:
            raise ValueError(str(e))

        unit_price = product.get("price")
        quantity = data["quantity"]
        total = unit_price * quantity
        data["total"] = total

        #Set purchase status
        data["status"] = "AC"

        # Get inventory by product ID
        inventory = InventoryService.get_inventory_by_product(data['idProduct'])
        if not inventory:
            raise ValueError("Inventory for the specified product not found.")

        current_quantity = inventory.get('quantity', 0)
        purchase_quantity = data['quantity']

        # Check if there is enough stock
        if purchase_quantity > current_quantity:
            raise ValueError("Insufficient inventory quantity for this purchase.")

        # Update inventory: subtract the purchased quantity
        new_quantity = current_quantity - purchase_quantity
        InventoryService.update_inventory({
            "idProduct": inventory['idProduct'],
            "quantity": new_quantity
        })

        PurchaseData.create_purchase(data)
        
        return data