from fastapi import FastAPI
from service.routes import api_router 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# Allow CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Agrega las rutas del router principal
app.include_router(api_router, prefix="/api")