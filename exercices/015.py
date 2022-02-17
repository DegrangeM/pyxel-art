from libs.PyxelArt import *

for y in range(9) :
    colorier(2,y)
for x in range(3,7) :
    colorier(x,1)
    colorier(x,3)
    colorier(x,5)
    colorier(x,7)
a = 0
for loop in range(5) :
    colorier(6,a)
    a = a + 2

ss()