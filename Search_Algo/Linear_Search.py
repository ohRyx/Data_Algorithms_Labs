def search(arr, x):
    for i in range(len(arr)):
        if (arr[i] == x):
            return i
    return -1

arr = [2,3,10,40]
x = 40

result = search(arr, x)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element %d is present at index %d" %(x, result))
