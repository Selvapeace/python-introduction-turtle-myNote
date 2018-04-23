# 模拟pow函数
def power(x,y):
    return x**y


# 用欧几里得算法求最大公约数
def gcd(x,y):
    if y == 0:
        return x
    elif x % y == 0:
        return y
    else:
        if x > y:
            a = x % y
            x = y
            y = a
        else:
            x,y = y,x
            a = x % y
            x = y
            y = a
        return gcd(x,y)

# 欧几里得算法改进：当x<y时，a = x%y = x，此时令x = y ,y = a相当于交换了x和y
# 因此无需区分x和y的大小
# 方法1用到递归，实际是一个‘无限循环’直到到达基例才停止，因此可用while循环等价
def gcd2(x,y):
    while y:
        a = x % y
        x = y
        y = a
    return x


# 十进制转二进制
def trans(num):
    count = 1
    if num >= 1:
        while 2**count <= num:
            count += 1
        b = ''
        for i in range(count):
            a = num % 2
            num = num // 2
            b = b + str(a)
        result = b[::-1]
        return result + 'B'
    else:
        result = ''
        for i in range(15):
            a = str(int(num * 2))
            num = num * 2 - int(num * 2)
            result = result + a
        return '0.' + result + 'B' + '(保留15位小数)'

# 十进制转二进制改进
# 方法1用字符串的形式加入数字，也可用列表
# 方法1需要计算二进制数值的位数，不能确定位数时还要保留15位小数，体验不好！用while
def trans2(num):
    temp = []
    result = ''
    if num >= 1:
        while num:
            a = num % 2
            num = num // 2
            temp.append(a)
        while temp:
            result += str(temp.pop())       # 把列表temp的元素从右到左依次取出并删除，变为字符串粘贴到result上
        result = result + 'B'
    else:
        while num:
            a = str(int(num * 2))
            num = num * 2 - int(num * 2)
            result += a
        result = '0.' + result + 'B'
    return result
    
