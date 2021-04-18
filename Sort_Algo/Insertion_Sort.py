def InsertionSort(array):
    for x in range(1, len(array)):
        value_to_sort = array[x]

        while array[x-1] > value_to_sort and x>0:
            array[x], array[x-1] = array[x-1], array[x]
            x = x-1

aList = [5,2,6,7,1]
InsertionSort(aList)
print(aList)
