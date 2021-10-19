from libs.PyxelArt import *

colorier(0,4)
colorier(2,4)

a = 6
b = 2

colorier(a,b)
a = a + 1
colorier(a,b)
a = a + 1
colorier(a,b)
b = b + 1
colorier(a,b)
b = b + 1
colorier(a,b)
a = a - 1
colorier(a,b)
a = a - 1
colorier(a,b)

c = 0
for loop in range(7) :
    colorier(c,3)
    c = c + 1

ss()