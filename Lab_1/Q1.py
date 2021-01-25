#Write  an  algorithm  that  returns  the  index  of  the  
# first  occurrence  of  the  largest element 
# in an array s[0],...,s[n-1].

def findLargestIndex(a):
  largeIndex = 0
  index = 0

  for x in a:
    if x > a[largeIndex]:
      largeIndex = index
    index +=1
  return largeIndex


array = input("Enter a list of numbers separated by commas:")
array = [int(x) for x in array.split(",")]

largestIndex = findLargestIndex(array)

print ("\nThe largest number is %d at index %d" %(array[largestIndex], largestIndex))
