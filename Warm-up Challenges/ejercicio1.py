import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    color_pos = []
    color_list = sorted(ar)
    i = 0

    print(color_list)

    while i < n - 1:
        if color_list[i] == color_list [i+1]:
            color_pos.append(i)
            color_pos.append(i+1)
            i+=2
        else:
            i+=1
        
    # print(len(color_pos))

    return len(color_pos)//2
        
# sockMerchant(9 , [10, 20, 20, 10, 10, 30, 50, 10, 20])
sockMerchant(15 , [6, 5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5])
