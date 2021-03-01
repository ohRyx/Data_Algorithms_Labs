def printBitString(n, binary):
    if n == 0: #O(1)
        print(binary)
    else:
        #Similar to Fibonnaci, O(2^n)
        printBitString(n-1, binary + "0")
        printBitString(n-1, binary + "1")

nBit=int(input("Enter the number of bits to print:\n")) 

print("The list of",nBit,"bit binary strings are:")
printBitString(nBit, "")