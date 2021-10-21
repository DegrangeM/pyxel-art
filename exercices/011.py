from libs.PyxelArt import *

x = 0
for loop in range(9) :
    y= 0
    for loop in range(9) :
        if x == 0 :
            if y >= 2 :
                if y <= 6 :
                    colorier(x,y)
        if x == 1 :
            if y >= 3 :
                if y <= 5 :
                    colorier(x,y)
        if x == 2 :
            if y == 4 :
                colorier(x,y)
        if x >= 3 :
            if x <= 7 :
                if y >= 2 :
                    if y <= 5 :
                        if x == 6 :
                            if y != 3 :
                                colorier(x,y)
                        else :
                            colorier(x,y)
        y = y + 1
    x = x + 1

colorier(3,3)
colorier(3,4)
colorier(5,6)
colorier(6,6)
colorier(7,6)
colorier(8,3)
colorier(8,4)
colorier(8,5)

ss()