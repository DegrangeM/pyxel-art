from libs.PyxelArt import *

a = 2
b = a
c = 1

for loop in range(5) :
    if a != 4 :
        colorier(a,1)
    else :
        colorier(a,2)
    a = a + 1
    
for loop in range(3) :
    colorier(1,b)
    colorier(7,b)
    b = b + 1

colorier(4,7)
for loop in range(2) :
    colorier(4-c,7-c)
    colorier(4+c,7-c)
    c = c + 1

ss()