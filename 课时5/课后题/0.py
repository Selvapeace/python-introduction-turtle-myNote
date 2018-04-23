import random

num = random.randint(1,10)
temp=input("which number?")


while temp.isdigit() == False:
    print("please input a 'number'!!!")
    temp=input("which number?")
# str.isdigit() 该字符串里都是数字，则True
# str.isalnum() 都是字母或数字
# str.isalpha() 都是字母
# str.islower() 都是小写
# str.isupper() 都是大写
# str.istitle() 都是首字母大写
# str.isspace() 都是空白字符
    
guess=int(temp)
if guess == num:
    print("6666666666")
    print("but no prize")
else:
    n=0
    while guess != num and n < 3:
        if guess < num:
            temp=input("the true number is bigger")
            guess=int(temp)
            n=n+1
        else:
            temp=input("the true number is smaller")
            guess=int(temp)
            n=n+1
print("game over")
