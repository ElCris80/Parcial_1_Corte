from fastapi import FastAPI

from caballero_endpoints import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Primer parcial de Desarrollo de Software"}

