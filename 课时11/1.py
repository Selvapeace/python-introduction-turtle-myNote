num = [1,2,3,4,5]

# 元素交换
a = num[0]
num[0] = num[3]
num[3] = a

# 删除元素
num.remove(1)    # 根据元素的名字删除
del num[2]      # 根据位置删除
del num      # 整个列表删除
num = [1,2,3,4,5]
b = num.pop()      # 默认删除最后一个元素并提出来命名
c = num.pop(1)     # 删除第二个元素并提出来命名

# 列表切片
num = [1,2,3,4,5]
num[1:3]
num[:3]
num[1:]
num[]
