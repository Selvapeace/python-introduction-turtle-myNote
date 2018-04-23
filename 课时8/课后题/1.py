# method 1
x,y,z = 6,5,4
small = x if x < y else y
small = small if small < z else z

# method 2
big = x if(x > y and x > z) else (y if y > z else z)
