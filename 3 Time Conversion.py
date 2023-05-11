#!/bin/python3

import math
import os
import random
import re
import sys
from time import strftime, strptime

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    return strftime("%H:%M:%S", strptime(s, "%I:%M:%S%p") )
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()


#All tests passed