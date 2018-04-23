old = [1,2,3]
new = old
old = 'hhh'
print(new)

list1 = [1,[1,2,['小甲鱼']],3,4,5]
list1[1][2][0] = '小鱿鱼'
print(list1)

list1 = ['1.just do it','2.一切皆有可能','3.让编程改变世界','4.impossible is nothing']
list2 = ['4.阿迪达斯','2.李宁','3.鱼c','1.耐克']
list3 = [x + ':' + y[2:] for i in range(1,5) \
         for x in list2 for y in list1 if eval(x[0]) == eval(y[0]) == i]

