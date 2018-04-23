leastnum = input("有一个长阶梯，若每步上2阶，最后剩1阶；若每步上3阶，最后剩2阶；若每步上5阶，最后剩4阶；若每步上6阶，最后剩5阶；只有每步上7阶，最后刚好一阶也不剩.猜猜该阶梯至少有几阶？")

while not leastnum.isdigit():
    print("请输入整数")
    leastnum = input("再猜一次")

n = 0
while n < 100:
    guess = int(leastnum)
    if guess%2 != 1 or guess%3 != 2 or guess%5 != 4 or guess%6 != 5 or guess%7 != 0:
        print("错了")
        leastnum = input("再猜一次")
        n += 1
    else:
        print("对啦")
        break
    
    
