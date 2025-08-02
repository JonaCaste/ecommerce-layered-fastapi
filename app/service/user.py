from fastapi import APIRouter, HTTPException, Request

from business.user import UserBusiness

user_router = APIRouter()

@user_router.post("/register")
async def register_user(request: Request):
    """
    Register a new user.

    - **Request body:** JSON containing user data (username, email, password, direction)
    - **Returns:** Success message or validation error
    """
    try:
        data = await request.json()
        result = UserBusiness.register_user(data)
        return result
    except ValueError as e:
        # Handle known validation or business logic errors
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail="Internal server error")

@user_router.post("/login")
async def login_user(request: Request):
    """
    Log in an existing user.

    - **Request body:** JSON with email and password
    - **Returns:** Authentication token or error
    """
    try:
        data = await request.json()
        result = UserBusiness.login_user(data)
        return result
    except ValueError as e:
        # Handle known validation or business logic errors
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Handle unexpected errors
        raise HTTPException(status_code=500, detail="Internal server error")