class Stack:
    def __init__(self):
        self.top = -1
        #this stack is implemented with Python list (array)
        self.data = []

    def push(self, value):
        #increment the size of data using append()
        self.data.append(0)
        self.top +-1
        self.data[self.top] = value
        
    def pop(self):
        value = self.data[self.top]
        #delete the top value using del
        del self.data[self.top]
        self.top -= 1
        return value

    def isEmpty(self):
        return (self.top == -1)

    def peek(self):
        return self.data[self.top]

    def printStack(self):
        print(self.data)
    
    def invert(self):
        value = self.data
        first = 0
        last = 0
        index = 0
        for x in value[::-1]:
            first = x
            last = value[index]
            x = last
            value[index] = first
            index += 1

array = input("Enter a list of numbers separated by commas:\n")
array = [int(x) for x in array.split(",")]
        
s = Stack()
for n in array:
  s.push(n)

s.printStack()
s.invert()
s.printStack()
s.invert()
s.printStack()