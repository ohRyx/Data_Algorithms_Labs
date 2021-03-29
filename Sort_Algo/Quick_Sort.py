def QuickSort(a):
    size = len(a)
    if size > 1:
        pivotIndex = partition(a)
        a[0:pivotIndex] = QuickSort(a[0:pivotIndex])
        a[pivotIndex +1:size] = QuickSort(a[pivotIndex+1:size])
    return a

def partition(a):
    pivot = a[0]
    size = len(a)
    pivotIndex = 0
    for index in range(1,size):
        if a[index] < pivot:
            pivotIndex += 1
            a[index], a[pivotIndex] = a[pivotIndex], a[index]
    a[0], a[pivotIndex] = a[pivotIndex], a[0]
    return pivotIndex

alist = [8,2,5,9,7,1]
print(QuickSort(alist))