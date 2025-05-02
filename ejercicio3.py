import math
import os
import random
import re
import sys

def repeatedString(s, n):
    count = n//len(s) 
    count_a = s.count('a') * count 
    
    if count * len(s) < n:
        extra_a = 0
        extra_letters = n - (count * len(s))
        extra_a = s[:extra_letters].count('a')
        count_a += extra_a

    return count_a  

repeatedString('gfcaaaecbg', 547602)    