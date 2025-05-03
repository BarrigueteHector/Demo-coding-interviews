import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    count = 0
    countValley = 0

    for p in path:
        last_count = count

        if p == 'U':
            count += 1
        else:
            count -= 1

        if count == -1 and last_count == 0:
            countValley += 1

    # print(countValley)
    return countValley


countingValleys(8, 'UDDDUDUU')