class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next= next
                    
class Stack:
    def __init__(self):
        self.top = None
        self.item_count = 0
        
    def is_empty(self):
        return self.top is None
    
    def push(self,data):
        n = Node(data,self.top)
        self.top = n
        self.item_count +=1
    
    def pop(self):
        if not self.is_empty():
            data = self.top.item
            self.top = self.top.next
            self.item_count -=1
            return data
        else:
            raise IndexError("Stack is empty:")
        
    def peek(self):
        if not self.is_empty():
            return self.top.item
        else:
            raise self.is_empty()
    
    def size(self):
        return self.item_count    
            
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(50)
s1.push(90)
print("Total elements in the Stack:",s1.size())
print("Top element in the stack:",s1.peek())
print("Pop element in the stack:",s1.pop())
print("Total elements in the Stack:",s1.size())
print("Top element in the stack:",s1.peek())
