# 学习tdqm模块的使用
# pip install tqdm

from tqdm import tqdm
import time

# 1.最简单的用法
# for i in tqdm(range(100)):
#     time.sleep(0.2)

# 2.使用with语句
# with tqdm(total=100) as pbar:
#     for i in range(100):
#         time.sleep(0.2)
#         # 设置一个数字表示更新的频率
#         pbar.update(1)

# 3.自定义进度条，例如添加前缀
# for i in tqdm(range(100), desc="[Processing]"):
#     time.sleep(0.1)
    
# 4.设置进度条的格式
# for i in tqdm(range(100),
#               desc='Processing',
#               ncols=80, # 进度条的宽度
#               unit='it', # 单位
#               unit_scale=True): # 自动缩放
#     time.sleep(0.1)

# 5.嵌套进度条
# from tqdm.auto import tqdm # 注意导入的模块不一样
# for i in tqdm(range(10), desc="Outer"):
#     for j in tqdm(range(50), desc="Inner", leave=False):
#         time.sleep(0.1)

# 6.手动更新进度条
# import random
# with tqdm(total=100) as pbar:
#     for j in range(100):
#         time.sleep(0.1)
        
#         # 设置前缀描述并实时更新
#         pbar.set_description(f"Process{j}")
#         # 设置后缀信息
#         # 变量名设置什么，就会显示什么变量
#         # pbar.set_postfix(qrc=f'{random.random():.3f}')

#         # 使用字典更新后缀
#         metrics = {
#             "loss": random.random(),
#             "acc": random.random(),
#             "lr": 0.001,
#         }
#         pbar.set_postfix(**metrics)


#         pbar.update(1)


