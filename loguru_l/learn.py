# pip install loguru

from loguru import logger



# 保存在app.log文件中，会进行续写
logger.add(
    "./loguru_l/app.log",
    rotation="00:00",
    compression='zip'
    )

# logger.add(
#     "my_app_{time}.log",
#     rotation="00:00",  # 每天切割 1 week/ 500 MB /
#     retention="30 days",  # 保留30天 日志保留天数
#     compression="zip",  # 压缩为zip
#     encoding="utf-8",
#     level="DEBUG",  # 文件里记录更详细的日志
#     enqueue=True  # 多进程安全
# )

# 日志过滤
# 只将 ERROR 及以上级别的日志记录到 error.log
logger.add("./loguru_l/error.log", filter=lambda record: record["level"].name == "ERROR")
# 只将包含 "hello" 的消息记录到 hello.log
logger.add("./loguru_l/success.log", filter=lambda record: "success" in record["message"].lower())


# 六种级别的日志输出
# 默认情况下，这些日志会以带颜色和格式的形式输出到控制台，包含时间、级别、模块名、行号和消息
logger.info("INFO")
logger.debug("DEBUG")
logger.critical("CRITICAL")
logger.error("ERROR")
logger.warning("WARNNING")
logger.success("SUCCESS")



# 捕捉函数中的异常

@logger.catch
def cal(x, y):
    return 1 / (x + y)

try:
    cal(0, 0)
except Exception:
    logger.exception("发生异常")

# logger.parse()

