# 找出所有水仙花数：如果一个三位数等于其各位数字的立方和，称其为水仙花数
def fun():
    for x in range(1,10):
        for y in range(10):
            for z in range(10):
                while x**3 + y**3 + z**3 == x * 100 + y * 10 + z:
                    print(x,y,z)
                    break


# 统计一个长度为2的子字符串在另一个字符串中出现的次数
# method 1
def findstr():
    mystr = input('请输入目标字符串：')
    key = input('请输入子字符串（两个字符）')
    count = 0
    while key in mystr:
        count += 1
        change = mystr.find(key)+2
        mystr = mystr[change:]
    print('子字符串在目标字符串中共出现',count,'次')
    
# method 2
def findstr2(mystr,key):
    count = 0
    for i in range(len(mystr)-1):
        if mystr[i] == key[0]:
            if mystr[i+1] == key[1]:
                count += 1
    print('子字符串在目标字符串中共出现',count,'次')
mystr = input('请输入目标字符串：')
key = input('请输入子字符串（两个字符）')
findstr2(mystr,key)
