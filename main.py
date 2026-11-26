from fastapi import APIRouter, FastAPI

app = FastAPI(title="Truckit API", version="0.1.0")

api_router = APIRouter(prefix="/api/v1")


@api_router.get("/health")
def health():
    return {"status": "ok"}


app.include_router(api_router)