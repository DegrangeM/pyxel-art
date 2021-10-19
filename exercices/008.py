from libs.PyxelArt import *

a = 3
for loop in range(4) :
    colorier(a,1)
    colorier(a,8)
    colorier(1,a)
    colorier(8,a)
    a = a + 1
    
colorier(2,2)
colorier(2,7)
colorier(7,7)
colorier(7,2)
colorier(4,3)

b = 4
for loop in range(3) :
    colorier(6,b)
    colorier(7,b)
    colorier(b,7)
    b = b + 1
    
colorier(7,3)
colorier(5,5)
colorier(4,5)
colorier(4,6)
colorier(3,6)
colorier(3,7)

    
ss()