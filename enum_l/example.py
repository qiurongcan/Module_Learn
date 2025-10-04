from enum import Enum, unique


@unique
class Color(Enum):
    RED:int = 1
    GREEN:int = 2
    BLUE:float = 3.0
    # BLACK:int = 1 # 加上unique以后，值不能重复！！！

print(Color.BLUE)
print(Color.BLUE.name)
print(Color.BLUE.value)

a = 3
print(a == Color.BLUE.value)

for color in Color:
    print(color.name, ": ", color.value)

# 数字遍历从1开始
print(Color(3))
print(Color['RED'].value)


