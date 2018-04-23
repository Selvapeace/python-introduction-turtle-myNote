import random

num = random.randint(1,10)
temp=input("which number?")
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
