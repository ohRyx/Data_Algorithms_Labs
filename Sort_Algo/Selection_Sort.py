def SelectionSort(list):
    for i in range(len(list)):
        min_index = i

        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        
        list[i], list[min_index] = list[min_index], list[i]


alist = [4,9,3,6,2]
SelectionSort(alist)
print(alist)



