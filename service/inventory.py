from fastapi import APIRouter, HTTPException, Request

from business.inventory import InventoryService

inventory_router = APIRouter()

@inventory_router.put("/update")
async def update_inventory(request: Request):
    """
    Update product inventory.

    - **Request body:** JSON with product ID and inventory change
    - **Returns:** Updated inventory data
    """
    try:
        data = await request.json()
        result = InventoryService.update_inventory(data)
        return result
    except ValueError as e:
        # Handle known validation or business logic errors
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail="Internal server error")