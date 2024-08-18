from fastapi import FastAPI # type: ignore
from app.routes import router as calendar_router # type: ignore

app = FastAPI()

app.include_router(calendar_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn # type: ignore
    uvicorn.run(app, host="0.0.0.0", port=8000)
