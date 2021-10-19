from libs.PyxelArt import *

a = 0
for loop in range(2) :
    colorier(3,a)
    colorier(4,a)
    colorier(5,a)
    a = a + 1

x = 3
for loop in range(3) :
    y = 3
    for loop in range(4) :
        colorier(x,y)
        y = y + 1
    x = x + 1

b = 2
colorier(2*b,b)

for loop in range(5) :
    if b != 4 :
        colorier(b,8)
    b = b + 1
    
colorier(3,7)
colorier(5,7)
colorier(1,3)
colorier(2,4)
colorier(6,4)
colorier(7,3)
    
ss()