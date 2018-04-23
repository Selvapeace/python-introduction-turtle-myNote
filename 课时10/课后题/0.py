a = ['小甲鱼',88,'黑夜',90,'迷途',85,'怡静',90,'秋舞斜阳',88]
for i in range(len(a)):
    print(a[i])

# mtehod 1
for i in range(len(a)):
    if i % 2 == 0 :
        print(a[i],end = ' ')
    else:
        print(a[i])

# method 2
for i in range(len(a)):
    if type(a[i]) == str :
        print(a[i],end = ' ')
    else:
        print(a[i])

# method 3
count = 0
l = len(a)
while count < l:
    print(a[count],a[count+1])
    count += 2
