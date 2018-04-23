sec = input('请输入密码：')
sectrue = 'jjj123'
n = 0
while n < 3:
    if '*' in sec:
        sec = input('密码中不能含有‘*’号！您还有3次机会！请输入密码：')
    elif sec != sectrue:
        m = 3 - n
        print('密码输入错误！您还有',m,'次机会！')
        sec = input('请输入密码：')
        n += 1
    else:
        print('密码正确，进入程序......')
        break
