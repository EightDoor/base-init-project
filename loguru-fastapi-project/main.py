import time
from contextlib import asynccontextmanager

from logger_configuration import logging_init
from fastapi import FastAPI, Request
import uvicorn
from loguru import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 运行期间
    logging_init()
    yield
    # 运行结束
    pass

app = FastAPI(lifespan=lifespan)

@app.middleware("http")
async def signature_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    formatted_time = "{0:.2f}".format(process_time)
    logger.debug(
        f"path: {request.url.path} | method: {request.method} | ip: {request.client.host} | response_status: {response.status_code} | response_time: {formatted_time}"
    )
    return response

@app.get("/")
def hello():
    logger.info("测试打印")
    logger.debug("测试打印debug")
    return "hello world"


if __name__ == "__main__":
    uvicorn.run("main:app", port=3001)