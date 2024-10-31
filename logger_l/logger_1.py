import logging

from colorama import Fore, Back, Style
import colorama

# 初始化 colorama
colorama.init()

# 创建带颜色的 formatter
class ColoredFormatter(logging.Formatter):
    FORMAT = "[%(asctime)s %(levelname)s]: %(message)s"
    
    FORMATS = {
        logging.DEBUG: Fore.BLUE + FORMAT + Style.RESET_ALL,
        logging.INFO: Fore.GREEN + FORMAT + Style.RESET_ALL,
        logging.WARNING: Fore.YELLOW + FORMAT + Style.RESET_ALL,
        logging.ERROR: Fore.RED + FORMAT + Style.RESET_ALL,
        logging.CRITICAL: Fore.RED + Back.WHITE + FORMAT + Style.RESET_ALL
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


# 创建配置 logger
logger = logging.getLogger("mylogger")
# 设置日志级别
logger.setLevel(logging.INFO)

# 创建文件处理器
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)

# 创建控制台输出 终端输出？
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# ----在此处可以创建自己喜欢的输出格式  格式见附录1---------
# 创建Formatter
# %(filename)s    文件名
# %(funcName)s    函数名
formatter = logging.Formatter('[%(lineno)d - %(asctime)s][%(filename)s][%(funcName)s] - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)  # 终端输出
file_handler.setFormatter(formatter)     # 文件中输出

# 将handler 添加到logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 使用logger, 不同的信息在输出到文件的时候会有不同的颜色
logger.debug("This debug msg")
logger.info("This info msg")
logger.warning("This warning msg")
logger.error("This error msg")
logger.critical("This critical msg")

def hello():
    logger.info("hello my first logger")

hello()

# 在文件中输出是有颜色的
# 附录1：
# 输出的格式有下列信息
# 常用基本属性：
# %(asctime)s     时间戳
# %(name)s        Logger的名字
# %(levelname)s   日志级别名称
# %(levelno)s     日志级别数字
# %(message)s     日志信息
# %(pathname)s    完整路径名
# %(filename)s    文件名
# %(funcName)s    函数名
# %(lineno)d      行号
# %(module)s      模块名
# %(process)d     进程ID
# %(processName)s 进程名
# %(thread)d      线程ID
# %(threadName)s  线程名