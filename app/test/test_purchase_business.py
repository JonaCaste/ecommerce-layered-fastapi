import pytest
from unittest.mock import patch
from business.purchase import PurchaseService

# ---------- Test purchase_product ----------

def test_purchase_product_success():
    data = {"idProduct": 1, "idUser": 2, "quantity": 3}
    mock_product = {"id": 1, "price": 100.0}
    mock_inventory = {"idProduct": 1, "quantity": 10}

    with patch("business.purchase.ProductBusiness.get_product_by_id", return_value=mock_product), \
         patch("business.purchase.InventoryService.get_inventory_by_product", return_value=mock_inventory), \
         patch("business.purchase.InventoryService.update_inventory") as mock_update_inventory, \
         patch("business.purchase.PurchaseData.create_purchase") as mock_create:

        result = PurchaseService.purchase_product(data)

        mock_create.assert_called_once()
        mock_update_inventory.assert_called_once()
        assert result["status"] == "AC"
        assert result["total"] == 300.0


def test_purchase_product_missing_idProduct():
    data = {"idUser": 2, "quantity": 3}
    result = PurchaseService.purchase_product(data)
    assert result["error"] == "'idProduct' is required."


def test_purchase_product_invalid_quantity_type():
    data = {"idProduct": 1, "idUser": 2, "quantity": "five"}
    result = PurchaseService.purchase_product(data)
    assert result["error"] == "'quantity' must be of type <class 'int'>."


def test_purchase_product_quantity_less_than_one():
    data = {"idProduct": 1, "idUser": 2, "quantity": 0}
    with pytest.raises(ValueError, match="The 'quantity' must be a non-negative integer."):
        PurchaseService.purchase_product(data)


def test_purchase_product_not_found():
    data = {"idProduct": 1, "idUser": 2, "quantity": 3}
    with patch("business.purchase.ProductBusiness.get_product_by_id", side_effect=ValueError("Product not found.")):
        with pytest.raises(ValueError, match="Product not found."):
            PurchaseService.purchase_product(data)


def test_purchase_product_insufficient_inventory():
    data = {"idProduct": 1, "idUser": 2, "quantity": 10}
    mock_product = {"id": 1, "price": 20.0}
    mock_inventory = {"idProduct": 1, "quantity": 5}

    with patch("business.purchase.ProductBusiness.get_product_by_id", return_value=mock_product), \
         patch("business.purchase.InventoryService.get_inventory_by_product", return_value=mock_inventory):

        with pytest.raises(ValueError, match="Insufficient inventory quantity for this purchase."):
            PurchaseService.purchase_product(data)


def test_purchase_product_persistence_error():
    data = {"idProduct": 1, "idUser": 2, "quantity": 2}
    mock_product = {"id": 1, "price": 80.0}
    mock_inventory = {"idProduct": 1, "quantity": 10}

    with patch("business.purchase.ProductBusiness.get_product_by_id", return_value=mock_product), \
         patch("business.purchase.InventoryService.get_inventory_by_product", return_value=mock_inventory), \
         patch("business.purchase.InventoryService.update_inventory"), \
         patch("business.purchase.PurchaseData.create_purchase", side_effect=Exception("DB failure")):

        with pytest.raises(Exception, match="DB failure"):
            PurchaseService.purchase_product(data)
