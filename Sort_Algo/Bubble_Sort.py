def BubbleSort(list):
    for i in range(len(list)):
        for j in range(1, len(list)):
            if list[j-1] > list[j]:
                temp = list[j]
                list[j] = list[j-1]
                list[j-1] = temp


aList = [8, 6, 5, 7]
BubbleSort(aList)
print(aList)
