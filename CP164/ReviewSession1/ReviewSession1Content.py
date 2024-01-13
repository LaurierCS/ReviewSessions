# Introduction to Classes

# Class: A blueprint for creating objects

class Name:
    
    def __init__(self, atr1, atr2):
        # called when an object is created, name_object = Name(atr1, atr2)
        self.first = atr1
        self.last = atr2
    
    def __str__(self):
        # called when str(Name) is called
        return self.atr1 + " " + self.atr2
    
    # many other magic/dunder methods

# Creating an object
name_object = Name("John", "Smith")

# Accessing attributes
print(name_object.first)
print(name_object.last)

# Calling methods
print(name_object.__str__())

# Array Based Stack (LIFO)
class Stack:
    
    def __init__(self):
        self.stack = []
    
    def __str__(self):
        return str(self.stack)
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0

# Drawing explanation
    
# Array Based Queue (FIFO)
class Queue:
    
    def __init__(self):
        self.queue = []
    
    def __str__(self):
        return str(self.queue)
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0

# Drawing explanation




