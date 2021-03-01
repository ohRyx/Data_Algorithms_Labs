#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr, arr_count):
    bird_freq = [0]*int(arr_count) #O(1)
    
    for i in range(len(arr)): #O(n)
        bird_freq[arr[i]] += 1 #O(1)
    return bird_freq.index(max(bird_freq)) #O(n)
    
arr_count = input("Enter a number of element: ")
arr = input("Enter a list of numbers separated by commas:")
arr = [int(x) for x in arr.split(",")]       
        
result = migratoryBirds(arr, arr_count)
        
print(result)