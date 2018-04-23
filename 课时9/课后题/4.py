a1,a2,a3 = '红','红','红'
b1,b2,b3 = '黄','黄','黄'
c1,c2,c3,c4,c5,c6 = '绿','绿','绿','绿','绿','绿'

import random
select = random.sample(range(1,13),k = 8)


# method
for red in range(0,4):
    for yellow in range(0,4):
        for green in range(2,7):
            if red + yellow + green ==8:
                print('红球',red,'黄球',yellow,'绿球',green)
