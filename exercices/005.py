from libs.PyxelArt import *

colorier(5,5)
colorier(6,4)

a = 0
for loop in range(9) :
    if a != 1 :
        colorier(4,a)
    if a < 3 :
        colorier(3,a)
        colorier(5,a)
    a = a + 1

colorier(3,7)
colorier(2,6)

ss()