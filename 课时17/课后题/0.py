'''
错误的函数定义：
def myfun((x,y),(a,b)):
    return x * y - a * b
因为参数不能用元组定义
'''
# 正确写法
def myfun(x,y):
    return x[0] * x[1] - y[0] * y[1]
print(myfun((3,4),(1,2)))
