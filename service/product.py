from fastapi import APIRouter, HTTPException, Request

from business.product import ProductBusiness

product_router = APIRouter()

@product_router.post("/")
async def create_product(request: Request):
    """
    Create a new product.

    - **Request body:** JSON with product details
    - **Returns:** Created product data or error
    """
    try:
        data = await request.json()
        result = ProductBusiness.create_product(data)
        return result
    except ValueError as e:
        # Handle known validation or business logic errors
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail="Internal server error")

@product_router.get('/')
def get_all_products():
    """
    Endpoint to retrieve all products.

    Returns:
        JSON response with list of products.
    """
    try:
        products = ProductBusiness.get_all_products()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")