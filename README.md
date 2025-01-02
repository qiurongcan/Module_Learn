# PYTHON Module Learn

## 0 git的使用以及github的代码版本管理

## 1 logging 库的使用

## 2 tqdm 库的使用

## 3 Cython编译的使用

创建`*.pyx`文件
```python
# rect.pyx
# 声明一个私有类
cdef class Rectangle():
    # 在初始化时，需要声明变量
    # cdef 表示编译后不能被外部调用
    # cpdef 表示编译后可以被外部调用
    # cdef public 性能较好，但是不能被重写 cpdef可以被重写
    cdef list line
    cdef int width, height

    def __init__(self, w=10, h=8):
        self.width = w
        self.height = h
        self.line = [1, 2, 3, 4]
    
    cpdef get_w(self):
        print(f"Rectangles's width is {self.width}")
        return self.width

    cpdef get_h(self):
        print(f"Rectangles's height is {self.height}")
        return self.height  

    cpdef cal_square(self):
        print(f"Rectangles's square is {self.width * self.height}")
        return self.width * self.height

    cpdef get_line(self):
        return self.line
```

创建setup.py文件
```python
from setuptools import setup
from Cython.Build import cythonize


setup(
    ext_modules=cythonize("rect.pyx")
)

```
进行编译
```shell
python setup.py build_ext --inplace
# 编译后会出现一个二进制文件
```


创建一个测试文件`test.py`
```python
rec = Rectangle()

width = rec.get_w()

square = rec.cal_square()

# 如果在类中没有声明cpdef width 或者 cdef public 则这行代码报错
# 声明则不报错
print(rec.width)

```

