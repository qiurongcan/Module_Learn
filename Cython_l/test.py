from rect import Rectangle


rec = Rectangle()

help(rec)
width = rec.get_w()

square = rec.cal_square()

# 如果在类中没有声明cpdef width 或者 cdef public 则这行代码报错
# 声明则不报错
# print(rec.width)


