# 装饰器的用法

from functools import wraps


import time 


# 装饰器的标准写法
def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        start_time = time.time()

        result = func(*args, **kargs)
        end_time = time.time()
        print(f"{func.__name__}执行时间：{end_time - start_time:.4f}s")

        return result
    
    return wrapper


@time_decorator
def calculate(a, b):
    time.sleep(0.2)
    return a + b


if __name__ == '__main__':

    print(calculate(4, 5))



"""
@warps(func)
复制元数据
__name__ 函数名
__doc__ 函数的文档字符串
__module__ 函数所在的模块
__annotations__ 函数的类型注解
__qualnmae__ 函数的限定名

"""
