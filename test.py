def binary_Search(array, x):
    left = array[0]
    right = len(array) - 1

    while left < right:
        mid = left + (right-left) // 2

        if array[mid] == x:
            return mid
        elif x < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

arr = [0,2,6,9,12,15]
x = 12
result = binary_Search(arr,x)

if result != -1:
    print("Element %d is present at index %d" %(x, result))
else:
    print("Element is not present")
