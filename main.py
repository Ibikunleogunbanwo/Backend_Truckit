from fastapi import FastAPI,HTTPException,Depends

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Truckit API!"}