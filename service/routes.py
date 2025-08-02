from fastapi import APIRouter
from .product import product_router
from .user import user_router
from .inventory import inventory_router
from .purchase import purchase_router

api_router = APIRouter()

# Include route groups
api_router.include_router(user_router, prefix="/users", tags=["User Management"])
api_router.include_router(product_router, prefix="/products", tags=["Product Management"])
api_router.include_router(inventory_router, prefix="/inventory", tags=["Inventory Management"])
api_router.include_router(purchase_router, prefix="/purchase", tags=["Purchase Management"])