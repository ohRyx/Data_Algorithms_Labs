
def reverse(a):
    first = 0
    last = 0
    index = 0

    for x in a[::-1]:
        first = x
        last = a[index]
        x = last
        a[index] = first
        index +=1

    
array = input("Enter a number: ")
array = [int(x) for x in array.split(",")]

reverse(array)
print(array)

     
