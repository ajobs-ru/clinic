import asyncio
import logging
import os
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from config import APP_PORT
from routers import api_router

# from tasks import start_scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await start_scheduler()
    yield


app = FastAPI(lifespan=lifespan, docs_url=None, redoc_url=None, openapi_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/documents", StaticFiles(directory="documents"), name="static")

app.include_router(router=api_router)


async def main():
    logging.basicConfig(level=logging.INFO)

    config = uvicorn.Config(app=app, host="0.0.0.0", port=APP_PORT)

    server = uvicorn.Server(config)

    await server.serve()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        try:
            os.sys.exit(130)
        except SystemExit:
            os._exit(130)
