from fastapi import APIRouter, HTTPException, Request

from business.purchase import PurchaseService

purchase_router = APIRouter()

@purchase_router.post("/")
async def purchase_product(request: Request):
    """
    Process a product purchase.

    - **Request body:** JSON with product ID, quantity, and shipping info
    - **Returns:** Purchase confirmation or error
    """
    try:
        data = await request.json()
        result = PurchaseService.purchase_product(data)
        return result
    except ValueError as e:
        # Handle known validation or business logic errors
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail="Internal server error")