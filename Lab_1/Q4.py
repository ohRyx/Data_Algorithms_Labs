#Given  an  array  s[0],...,s[n-1]  such  that  n  >  1  
# and  s[i]  ≤  s[i+1]  for  all  i.  
# Write  an algorithm that inserts an input value x into the array 
# so that s[i] ≤ s[i+1] for all i.

def orderInsert(a,value):
    index = 0
    for x in a:
        if value > x:
            index += 1
    a.insert(index, value)

array = input("Enter a list of numbers separated by commas:\n")
number = int(input("Enter a number to be inserted into the list: \n"))
array = [int(x) for x in array.split(",")]

orderInsert(array,number)
print(array)