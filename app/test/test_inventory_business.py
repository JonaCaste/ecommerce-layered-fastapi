# test_inventory_service.py

import pytest
from business.inventory import InventoryService
from data.inventory import InventoryData

# Simulate InventoryData (mock)
class MockInventoryData:
    @staticmethod
    def update_inventory_quantity(product_id, quantity):
        if product_id == 999:
            raise Exception("Database error")

    @staticmethod
    def get_inventory_by_product(product_id):
        if product_id == 999:
            raise Exception("Database error")
        return {"idProduct": product_id, "quantity": 10}


# Mock instance
InventoryService.InventoryData = MockInventoryData


# ---------- Test update_inventory ----------

def test_update_inventory_success(monkeypatch):
    def mock_update_inventory_quantity(product_id, quantity):
        assert product_id == 1
        assert quantity == 5

    monkeypatch.setattr(InventoryData, "update_inventory_quantity", mock_update_inventory_quantity)

    data = {"idProduct": 1, "quantity": 5}
    result = InventoryService.update_inventory(data)
    assert result == data


def test_update_inventory_missing_id():
    data = {"quantity": 5}
    with pytest.raises(ValueError, match="The field 'idProduct' is required."):
        InventoryService.update_inventory(data)


def test_update_inventory_invalid_quantity():
    data = {"idProduct": 1, "quantity": -3}
    with pytest.raises(ValueError, match="The 'quantity' must be a non-negative integer."):
        InventoryService.update_inventory(data)


def test_update_inventory_db_error(monkeypatch):
    def mock_update_inventory_quantity(product_id, quantity):
        raise Exception("DB error")

    monkeypatch.setattr(InventoryData, "update_inventory_quantity", mock_update_inventory_quantity)

    with pytest.raises(Exception, match="DB error"):
        InventoryService.update_inventory({"idProduct": 1, "quantity": 5})


# ---------- Tests get_inventory_by_product ----------

def test_get_inventory_success(monkeypatch):
    def mock_get_inventory_by_product(product_id):
        return {"idProduct": product_id, "quantity": 20}

    monkeypatch.setattr(InventoryData, "get_inventory_by_product", mock_get_inventory_by_product)

    result = InventoryService.get_inventory_by_product(1)
    assert result == {"idProduct": 1, "quantity": 20}


def test_get_inventory_invalid_id():
    with pytest.raises(ValueError, match="The 'product_id' is not valid"):
        InventoryService.get_inventory_by_product(-10)


def test_get_inventory_db_error(monkeypatch):
    def mock_get_inventory_by_product(product_id):
        raise Exception("DB error")

    monkeypatch.setattr(InventoryData, "get_inventory_by_product", mock_get_inventory_by_product)

    with pytest.raises(Exception, match="DB error"):
        InventoryService.get_inventory_by_product(1)
