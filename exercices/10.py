from libs.PyxelArt import *

colorier(4,8)

a = 0
b = -1
for loop in range(3) :
    colorier(1+a,6)
    colorier(1+a,6+b)
    colorier(a,6+b)
    colorier(2+a,6+b)
    colorier(1+a,6-b)
    a = a + 3
    b = -1 * b
    
c = 1
for loop in range(2) :
    colorier(4+c,0)
    colorier(4+2*c,0)
    colorier(4+c,1)
    colorier(4+2*c,1)
    colorier(4+3*c,1)
    colorier(4+c,8)
    colorier(4+2*c,8)
    colorier(4+2*c,7)
    c = -1
    
d = 0
for loop in range(5) :
    colorier(4,d)
    d = d + 1

ss()