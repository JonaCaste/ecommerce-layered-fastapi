import pytest
from unittest.mock import patch
from business.product import ProductBusiness

# ---------- Tests create_product ----------

def test_create_product_success():
    data = {"name": "Laptop", "price": 1200.0, "description": "Gaming laptop"}
    with patch("data.product.ProductData.create_product") as mock_create:
        result = ProductBusiness.create_product(data)
        mock_create.assert_called_once_with(data)
        assert result == data

def test_create_product_missing_name():
    data = {"price": 100.0, "description": "Item"}
    with pytest.raises(ValueError, match="The field 'name' is required."):
        ProductBusiness.create_product(data)

def test_create_product_invalid_price_type():
    data = {"name": "Pen", "price": "cheap", "description": "Blue ink"}
    with pytest.raises(ValueError, match="The field 'price' must be a number"):
        ProductBusiness.create_product(data)

def test_create_product_persistence_error():
    data = {"name": "TV", "price": 500.0, "description": "Smart TV"}
    with patch("data.product.ProductData.create_product", side_effect=Exception("DB Error")):
        with pytest.raises(Exception, match="DB Error"):
            ProductBusiness.create_product(data)

# ---------- Test get_product_by_id ----------

def test_get_product_by_id_success():
    expected = {"id": 1, "name": "Mouse", "price": 25.0, "description": "Wireless"}
    with patch("data.product.ProductData.get_product_by_id", return_value=expected):
        result = ProductBusiness.get_product_by_id(1)
        assert result == expected

def test_get_product_by_id_invalid_id():
    with pytest.raises(ValueError, match="Product ID is not valid."):
        ProductBusiness.get_product_by_id(-9)

def test_get_product_by_id_not_found():
    with patch("data.product.ProductData.get_product_by_id", return_value=None):
        with pytest.raises(ValueError, match="Product not found."):
            ProductBusiness.get_product_by_id(999)

def test_get_product_by_id_persistence_error():
    with patch("data.product.ProductData.get_product_by_id", side_effect=Exception("DB Failure")):
        with pytest.raises(Exception, match="DB Failure"):
            ProductBusiness.get_product_by_id(1)

# ---------- Test get_all_products ----------

def test_get_all_products_success():
    expected = [{"id": 1, "name": "Keyboard"}, {"id": 2, "name": "Monitor"}]
    with patch("data.product.ProductData.get_all_products", return_value=expected):
        result = ProductBusiness.get_all_products()
        assert result == expected

def test_get_all_products_persistence_error():
    with patch("data.product.ProductData.get_all_products", side_effect=Exception("Read error")):
        with pytest.raises(Exception, match="Read error"):
            ProductBusiness.get_all_products()
