def MergeSort(arr):
    size = len(arr)

    if size == 1:
        return arr
    
    mid = size // 2
    left = arr[0:mid]
    right = arr[mid:size]

    MergeSort(left)
    MergeSort(right)
    arr = merge(left, right)
    print(arr)

    return arr
    

def merge(aList, bList):
    cList = []
    sizeA = len(aList)
    sizeB = len(bList)

    indexA = indexB = 0
    while indexA < sizeA and indexB < sizeB:
        if alist[indexA] <= bList[indexB]:
            cList.append(alist[indexA])
            indexA += 1
        else:
            cList.append(bList[indexB])
            indexB +=1
    
    for i in range(indexA, sizeA):
        cList.append(aList[i])

    for i in range(indexB, sizeB):
        cList.append(bList[i])
    
    return cList


alist = [12,6,4,98,76,54]
MergeSort(alist)
print(alist)

