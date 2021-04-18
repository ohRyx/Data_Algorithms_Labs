#Write an algorithm that output the smallest and the 
# second smallest values in the array s[0],...s[n-1]. 
# Assume that n>1 and the values in the array are distinct

def find2Smallest(a):
    small = [a[0], a[0]]
    for x in a:
        if x < small[0]:
            small[1] = small[0]
            small[0] = x
    return small

array = input("Enter a list of numbers separated by commas:\n")
array = [int(x) for x in array.split(",")]

print("The two smallest values are:", find2Smallest(array))