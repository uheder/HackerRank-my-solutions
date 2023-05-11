#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    posNum = 0
    negNum = 0
    zerNum = 0
    for i in arr:
        if i > 0:
            posNum += 1
        elif i <0:
            negNum += 1
        elif i == 0:
            zerNum += 1
    print(posNum/n)
    print(negNum/n)
    print(zerNum/n)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


#code proceeded to pass all standard tests
