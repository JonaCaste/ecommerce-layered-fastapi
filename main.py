from fastapi import FastAPI
from service.routes import api_router 

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# Agrega las rutas del router principal
app.include_router(api_router, prefix="/api")