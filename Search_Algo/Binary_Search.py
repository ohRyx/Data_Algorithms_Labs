def BinarySearch(arr, x):
    left = arr[0]
    right = len(arr) - 1
    while(left < right):
        mid = (left + right-1) // 2

        if arr[mid] == x:
            return mid
        # If x is less than Mid, shift the right pviot to the left
        elif x < arr[mid]:
            right = mid - 1
        # Else if x is more than Mid, shift the left pivot to the right
        else:
            left = mid + 1
    return -1
    

arr = [0,2,6,9,12,15]
x = 9
result = BinarySearch(arr,x)

if result != -1:
    print("Element %d is present at index %d" %(x, result))
else:
    print("Element is not present")
