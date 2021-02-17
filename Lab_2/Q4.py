class SinglyListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    #return the value of the node at index

    def search(self, index):
        temp = self.head
        prev = None
        counter = 0
        while temp is not None and counter < index:
            prev = temp
            temp = temp.next
            counter += 1

        if temp is None:
            print('search error: invalid index')
        else:
            return temp

    def insertAtHead(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def delete(self, value):
        prev = None
        temp = self.head

        while temp != None and temp.data != value:
            prev = temp
            temp = temp.next

        #node to be deleted is head
        if temp == self.head:
            self.deleteAtHead()

        #Value found
        elif temp != None:
            prev.next = temp.next
            del temp
        #Value not found
        else:
            print('Value ', value, ' cannot be found')

    #delete the node at index
    def deleteAt(self,index):
        temp = self.head
        prev = None
        counter = 0
        while temp is not None and counter < index:
            prev = temp
            temp = temp.next
            counter += 1

        if temp is None:
            print('search error: invalid index')
        else:
            if prev is None:
                self.head = temp.next
            else:
                prev.next = temp.next
            del temp

    def deleteAtHead(self):
        temp = self.head
        self.head = self.head.next
        del temp

    def printList(self):
        temp = self.head
        output = "[ "
        while temp is not None:
            output += str(temp.data) + " "
            temp = temp.next
        output += "]"
        print(output)

    #return the number of elements in the queue
    def size(self):
        temp = self.head
        size = 0
        while temp is not None:
            size += 1
            temp = temp.next
        return size

def mergeList(s1, s2):
    s3 = SinglyLinkedList()
    tmp1 = s1.head
    tmp2 = s2.head
    tmp3 = s3.head
    
    if tmp1 is not None and tmp2 is not None:
        if tmp1.data < tmp2.data:
            s3.head = tmp1
            tmp3 = tmp1
            tmp1 = tmp1.next
        else:
            s3.head = tmp2
            tmp3 = tmp2
            tmp2 = tmp2.next
    else:
        if s1.head is None:
            s3.head = tmp2
        else:
            s3.head = tmp1
            
               
    while tmp1 is not None:
        if tmp2 is not None:
            if tmp1.data < tmp2.data:
                tmp3.next = tmp1
                tmp1 = tmp1.next
                tmp3 = tmp3.next
            else:
                tmp3.next = tmp2
                tmp2 = tmp2.next
                tmp3 = tmp3.next
        else:
            tmp3.next = tmp1
            tmp1 = tmp1.next
            tmp3 = tmp3.next
    
    
    while tmp2 is not None:
        tmp3.next = tmp2

array1 = input("Enter a list of numbers in descending order for list 1 separated by commas:\n")
array1 = [int(x) for x in array1.split(",")]

array2 = input("Enter a list of numbers in descending order for list 2 separated by commas:\n")
array2 = [int(x) for x in array2.split(",")]

s1 = SinglyLinkedList()
s2 = SinglyLinkedList()

#insert items into s1, starting with the largest number at the end of the array1
for i in range(len(array1)-1, -1, -1) :
  n = SinglyListNode(array1[i])
  s1.insertAtHead(n)

#insert items into s2, starting with the largest number at the end of the array2  
for i in range(len(array2)-1, -1, -1) :
  n = SinglyListNode(array2[i])
  s2.insertAtHead(n)

print("Content of list 1") 
s1.printList()
print("Content of list 2")
s2.printList()

s3 = mergeList(s1,s2)
print("Content of merged list")
s3.printList()