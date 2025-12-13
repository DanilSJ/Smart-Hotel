from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(
    lifespan=lifespan,
    title="Smart Hotel API",
    description="API Smart Hotel",
    version="0.1.0",
)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=7777)