#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def getMax(nums):
    max = nums[0]
    for i in nums[1:]:
        if i > max:
            max = i
    return max

def getMin(nums):
    min = nums[0]
    for i in nums[1:]:
        if i < min:
            min = i
    return min


def countingSort(arr):
    max = getMax(arr)
    # min = getMin(arr)
    counter = [0] * 100
    for i in arr:
        counter[i] += 1
    # result = []
    # for i in range(len(counter)):
    #     for j in range(counter[i]):
    #         result.append(i)
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
