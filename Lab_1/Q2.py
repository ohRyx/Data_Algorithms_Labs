#Write an algorithm that reverses the array s[0],...,s[n-1].

def reverse(a):
    first = 0
    last = 0
    index = 0

    for x in a[::-1]:
        first = x
        last = a[index]
        a[index] = first
        index +=1


array = input("Enter a list of numbers separated by commas:\n")
array = [int(x) for x in array.split(",")]

reverse(array)
print (array)
