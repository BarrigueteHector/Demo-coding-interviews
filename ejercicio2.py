import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    len_c = len(c)
    count_steps = 0

    bad_cloud = 0
    good_cloud = 0

    for i in c:
        if i == 0:
            good_cloud+=1
            bad_cloud = 0
        else:
            bad_cloud = 1
            good_cloud = 0

        # sprint("GC: ", good_cloud)

        if bad_cloud == 0:
            if good_cloud == 1 or good_cloud == 2 or good_cloud == 4 or good_cloud == 6 or good_cloud == 8:
                count_steps+=1
            elif good_cloud == 3 or good_cloud == 5 or good_cloud == 7:
                continue
        
        #print("CS: ", count_steps)
        
    print(count_steps-1)
    return count_steps - 1

jumpingOnClouds([0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]);

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     c = list(map(int, input().rstrip().split()))

#     result = jumpingOnClouds(c)

#     fptr.write(str(result) + '\n')

#     fptr.close()