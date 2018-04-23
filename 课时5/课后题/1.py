
year = input("please input a number of year")

while year.isdigit() == False:
    print("please input a 'number'!!!try again")
    temp=input("please input a number of year")

    
guess = int(year)
if guess%4 == 0 and guess%100 != 0:
    print("闰年")
elif guess%400 == 0:
    print("闰年")
else:
    print("不是闰年")
