for i in range(100,999,1):
    a = i//100
    b = (i - a * 100)//10
    c = i - a * 100 - b * 10
    if i == a**3 + b**3 + c**3:
        print(i,'是水仙花数')
    else:
        continue
