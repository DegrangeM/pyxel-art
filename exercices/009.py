from libs.PyxelArt import *

a = 0
for loop in range(3) :
    colorier(4+a,1)
    colorier(7,1+a)
    colorier(4,4+a)
    a = a + 1
    
a = 0
for loop in range(2) :
    colorier(2,2+a)
    colorier(5+a,4)
    a = a + 1
    
colorier(4,4*a)
colorier(a+1,a-1)

ss()