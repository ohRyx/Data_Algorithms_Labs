#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort() #O(nlogn)
    pairs = [] #0(1)
    current_min = sys.maxsize #O(1)
    for i in range(1,len(arr)): #O(n)
        diff = abs(arr[i] - arr[i - 1]) #O(1)
        #If Else comparison is O(1)
        if (diff < current_min):
            pairs = [arr[i-1], arr[i]]
            current_min = diff
        elif (diff == current_min):
            pairs.append(arr[i-1])
            pairs.append(arr[i])
    return pairs
    
arr = input("Enter a list of numbers separated by commas:")
arr = [int(x) for x in arr.split(",")]      

result = closestNumbers(arr)
print(result)

 