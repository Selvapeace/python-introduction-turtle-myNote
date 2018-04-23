# 序列

a = list()
print(a)

b = ' i love fish.com'
b = list(b)     #  把字符单个拆开，变成列表
print(b)

c = (1,2,4,5,6,765,867)
c = list(c)
print(c)

b = tuple(b)     # 把字符单个拆开，变成元组
print(b)

str(c)
len(c)
max(c)
max(b)    # 字母排序根据编码
min(b)    # 使用max和min，类型要相同
sum(c)
sum(c,6)   # 再加上6

sorted(c)    # 从小到大排序
reversed(c)   # 返回迭代器对象
list(reversed(c))  # 从大到小排序
list(enumerate(c))   # 返回(索引值，值）
list(zip(b,c))     # 返回（b的元素，c的元素），不能配对的直接省略

