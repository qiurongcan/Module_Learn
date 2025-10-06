
# property 将方法转化为属性
from math import pi

class Circle:

    def __init__(self, r = 10):
        self._r = r

    @property
    def r(self):
        return self._r

    # 属性设置
    @r.setter
    def r(self, value):
        if value < 0:
            raise  ValueError("半径需要设置为正值")
        else:
            print("半径已经修改")
            self._r = value
    # 删除变量
    @r.deleter
    def r(self):
        print('半径已经被删除')
        del self._r

    # 可供外部调用的方法
    @staticmethod
    def cal(r):
        return r**3
    



if __name__ == "__main__":

    c = Circle(r = 5)
    print(c.r)
    c.r = 100
    print(c.r)
    # c.r = -1
    # print(c.r)
    c.r = 7
    print(c.r)
    del c.r
    # 删除以后可以重新赋值
    c.r = 10
    print(c.r)
    res = Circle.cal(9)
    print(res)
    

    # print(c.area)

    # # c.r = 10
    # c._r = 10
    # # c._r = 100
    # print(c.area)
    

