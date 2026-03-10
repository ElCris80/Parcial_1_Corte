from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def root():
    return {"message": "Primer parcial de Desarrollo de Software"}

