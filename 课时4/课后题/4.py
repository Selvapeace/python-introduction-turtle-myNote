num = int(input("please input a number"))
while num:
    i = num
    while i:
        print(" ",end = " ")    # end = " "使得每次循环用空格代替换行
        i -= 1
    j=num
    while j:
        print("*",end = " ")
        j -= 1
    print()        #print()自动打印一个换行符
    num -= 1
