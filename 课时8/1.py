# elif = else if
score = int(input("请输入成绩："))
if 100 >= score >= 90:
    print("A")
elif 90 > score >= 80:
    print("B")
elif 80 > score >= 70:
    print("C")
elif 70 > score >= 60:
    print("D")
elif 60 > score:
    print("F")
else:
    print("输入错误")

import random
x = random.randint(1,10)
y = 3
small = x if x < y else y    #三元操作符
# 取x和y中较小的值


assert  #断言，assert后的条件为假时程序崩溃AssertionError.用于置入检查点，当需要确保某个条件为真才能正常工作时可用。
assert 3 > 4
