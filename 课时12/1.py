list1 = [123]
list2 = [234]
list1 > list2

list1 = [123,456]
list2 = [234,123]
list1 > list2               # 默认只比较第一对元素

list3 = list2
list1 < list2 and list3 == list2

list4 = list1 + list2    # 拼接    # 加号两端类型必须一致

list3 * 3
list3 *= 3

123 in list3

list5 = [1,2,3,['turtle','hhh']]
'turtle' in list5      # 对列表中列表的元素不能准确判断
'turtle' in list5[3]    # 可以！
list5[3][1]     # 取出'hhh'

list3.count(123)    # 列表中元素123的个数

list3.index(123,3,6)      # 索引：从位置3到位置6查找是否有元素123，并给出123的位置

list3.reverse()      # 列表元素逆序

list6 = [1,3,5,6,34,664,2,7]
list6.sort()      # 用指定方法对列表排序，默认从小到大
list6.sort(reverse = True)

# 列表copy两种方法的区别
list7 = list6[:]    # 拷贝之后就与原列表无关了
list8 = list6       # 拷贝之后，原列表变化，副本随之变化(相当于原列表多了一个标签）
list6.sort()


list1.copy()
list1.clear()

# 列表推导式
[ i*i for i in range(10)]   # 等价于下述

list1 = []
for i in range(10):
    list1.append(i**2)

list2 = [(x,y) for x in range(10) for y in range(10) \
         if x%2 == 0 if y%2 != 0]
