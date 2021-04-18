def MergeSort(array):
    if len(array) > 1:
        mid = len(array) //2
        left = array[:mid]
        right = array[mid:]
        
        # Recursion
        MergeSort(left)
        MergeSort(right)

        # Merge
        l = 0 # Left Array Index
        r = 0 # Right Array Index
        i = 0 # Merged Array Index

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                array[i] = left[l]
                l +=1
            else:
                array[i] = right[r]
                r +=1
            i +=1
        
        while l < len(left):
            array[i] = left[l]
            l +=1
            i +=1
        
        while r < len(right):
            array[i] = right[r]
            r += 1
            i += 1


alist = [12,6,4,98,76,54]
MergeSort(alist)
print(alist)

