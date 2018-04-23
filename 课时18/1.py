# 函数文档
def func(a):
    '这是func函数的函数文档；a是形参'
    print('传递进来的' + a + '是实参，因为它是具体的值')
func.__doc__       # 查看函数文档
help(func)        # 查看函数文档

def test(*b):
    print('参数的个数为：',len(b))
    print('第二个参数是：',b[1])
test(1,32,43543,'哈哈哈')

