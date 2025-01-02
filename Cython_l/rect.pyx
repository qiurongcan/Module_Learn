

cdef class Rectangle():
    """
    在初始化时，需要声明变量
    cdef 表示编译后不能被外部调用
    cpdef 表示编译后可以被外部调用
    cdef public 性能较好，但是不能被重写 cpdef可以被重写
    """

    cdef list line
    cdef int width, height

    def __init__(self, w=10, h=8):
        """
        初始化参数
        """
        self.width = w
        self.height = h
        self.line = [1, 2, 3, 4]

    cpdef get_w(self):
        """
        获取宽度
        """
        print(f"Rectangles's width is {self.width}")
        return self.width

    cpdef get_h(self):
        """
        获取长度
        """
        print(f"Rectangles's height is {self.height}")
        return self.height  

    cpdef cal_square(self):
        print(f"Rectangles's square is {self.width * self.height}")
        return self.width * self.height

    cpdef get_line(self):
        return self.line