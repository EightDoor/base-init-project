import os
import sys

from loguru import logger

work_path = os.path.split(os.path.realpath(__file__))[0]
logs_path = os.path.join(work_path, "./logs")


def logging_init():
    # 确保日志目录存在
    os.makedirs(logs_path, exist_ok=True)
    # 移除默认的logger
    logger.remove()

    logger.add(
        os.path.join(logs_path, "app_{time:YYYY-MM-DD}.log"),  # 文件名包含日期
        rotation="00:00",  # 每天午夜轮转
        level="DEBUG",
        retention="30 days",  # 保留30天日期
        compression="zip",  # 压缩旧日志
        enqueue=True,  # 线程安全
        backtrace=True,  # 记录异常堆栈
        diagnose=True,  # 诊断模式
        # format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {process.id} | {thread.name} | {name}:{function}:{line} - {message}",
    )
    logger.add(
        sys.stdout,
        colorize=True,
        # format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    )
    pass
