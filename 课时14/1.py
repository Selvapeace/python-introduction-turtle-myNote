# 字符串跟元组一样，创建之后不能更改
str1 = 'I love fish'
str1[5]
str1[:2] + '插入的字符串' + str1[2:]

str2 = 'hhhh'
str2.capitalize()       # 首字母大写
str3 = 'HHHH'
str3.casefold()     # 全小写
str3.center(40)     # 总长度为40，字符串居中
str3.count('h')      # 计数，有几个h
str2.endswith('h')    # 是否以h结束
str2.startswith('h')
'123456'.find('6')     # 从左开始检测6是否包含在字符串中，有则返回第一个索引值，无则返回-1
'61234566'.rfind('6')      # 从右开始检测
'123456'.index('6')    # 类似find，但若不存在6，则报错
'123456'.rindex('6')

'123456'.isalnum()
'123456'.isalpha()
'123456'.isdecimal()
'123456'.isdigit()
'123456'.islower()
'123456'.isnumeric()
'123456'.isspace()
'123456'.isupper()
'hhh'.istitle()

'123456'.join('hh')     # 以123456为分隔符，将分隔符插入到hh每个字符之间
'123456'.ljust(30)      # 总长度为30，字符串左对齐
'123456'.rjust(30)
'HHH'.lower()       # 小写
'hhh'.upper()
'      123456'.lstrip()      # 去掉字符串左侧所有空格
'123456     '.rstrip()
'i love fish'.partition('ov')    # 以ov为界限，将字符串分成3份
'i love fish'.rpartition('ov')
'123456'.replace('1','7')

'i love fish'.split()       # 默认按空格切分
'i love fish'.split('i')
'hhH'.swapcase()        # 翻转大小写
'hhh'.title()     # 标题化

'shufiahf5616463'.translate(str.maketrans('s','b'))   # 把s换成b  # str.maketrans('s','b')返回的是s和b的编码
'ggggdfsa'.zfill(50)      # 总长度为50，字符串右对齐，左侧用0填充
