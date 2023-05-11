#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    sum_array = sum(arr)
    minN = sum(arr)
    maxN = 0
    for i in arr:
        n = sum_array - i
        if n > maxN:
            maxN = n
        elif n < minN:
            minN = n
        
    print(minN, maxN)
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


#test failed 1/15 test cases