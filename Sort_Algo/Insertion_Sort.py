def InsertionSort(list):
    for index in range(1, len(list)):
        current = list[index]
        position = index -1

        while list[position] > current and position >= 0:
            list[position + 1] = list[position]
            position = position -1
        
        list[position + 1] = current

aList = [5,2,6,7,1]
InsertionSort(aList)
print(aList)
