class Stack:
    def __init__(self):
        self.top = -1
        #this stack is implemented with Python list (array)
        self.data = []

    def push(self, value):
        #increment the size of data using append()
        self.data.append(0)
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        value = self.data[self.top]
        #delete the top value using del
        del self.data[self.top]
        self.top -= 1
        return value

    def isEmpty(self):
        return (self.top == -1)

    def printStack(self):
        print(self.data)
        
def checkBrace(value):
    stack1 = Stack()
    
    for x in range(len(value)):
        stack1.push(value[x])
        stack1.printStack
    
    counter1 = 0
    counter2 = 0
    counter3 = 0
    temp = 0
    for x in range(len(value)):
        temp = stack1.pop()
        if temp is "(":
            counter1 += 1
        elif temp is ")":
            counter1 -= 1
        elif temp is "{":
            counter2 += 1
        elif temp is "}":
            counter2 -= 1
        elif temp is "[":
            counter3 += 1
        elif temp is "]":
            counter3 -= 1
        
    
    if counter1 is 0 and counter2 is 0 and counter3 is 0:
        return 1
    else:
        return None    
  
array = input("Enter a string to check:\n")

if checkBrace(array):
  print("The string",array,"is balanced")
else:
  print("The string",array,"is not balanced")