"""
Service layer for product management.
"""

from typing import Dict, List
from data.product import ProductData

class ProductBusiness:
    @staticmethod
    def create_product(data: Dict) -> Dict:
        """
        Creates a new product.

        Required fields:
        - name (str): The name of the product.
        - price (float): The price of the product.
        - description (str): The product's description.

        :param data: Dictionary with product details.
        :return: Dictionary with the result of the creation process.
        :raises ValueError: If any required field is missing or has an invalid type.
        """

        # Validate 'name'
        name = data.get("name")
        if name is None:
            raise ValueError("The field 'name' is required.")
        if not isinstance(name, str):
            raise ValueError("The field 'name' must be of type string.")

        # Validate 'price'
        price = data.get("price")
        if price is None:
            raise ValueError("The field 'price' is required.")
        if not isinstance(price, (int, float)):
            raise ValueError("The field 'price' must be a number (float or int).")

        # Validate 'description'
        description = data.get("description")
        if description is None:
            raise ValueError("The field 'description' is required.")
        if not isinstance(description, str):
            raise ValueError("The field 'description' must be of type string.")

        
        ProductData.create_product(data)

        return data
    
    @staticmethod
    def get_product_by_id(product_id: int) -> Dict:
        """
        Retrieves a product by its ID and validates the input.

        :param product_id: The ID of the product to retrieve.
        :return: A dictionary containing the product data.
        :raises ValueError: If product_id is invalid or product does not exist.
        """
        if not isinstance(product_id, int) or product_id <= 0:
            raise ValueError("Product ID is not valid.")

        product = ProductData.get_product_by_id(product_id)
        if not product:
            raise ValueError("Product not found.")

        return product
    
    @staticmethod
    def get_all_products() -> List[Dict]:
        """
        Retrieves all products from the database.

        Returns:
            list[dict]: List of all product records.
        """
        return ProductData.get_all_products()
