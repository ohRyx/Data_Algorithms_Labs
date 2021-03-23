def BinarySearch(arr, l, r, x):
    while(l < r):
        mid = l + (r-1) //2

        if arr[mid] == x:
            return mid
        # If x is less than Mid, shift the right pviot to the left
        elif x < arr[mid]:
            r = mid - 1
        # Else if x is more than Mid, shift the left pivot to the right
        else:
            l = mid + 1
    
    return -1


arr = [0,2,6,9,12,15]
x = 6
result = BinarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present")
