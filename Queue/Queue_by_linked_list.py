### Extending by singly linked list
class Node:
    def __init__(self,item =None,next=None):
        self.item = item
        self.next = next
        
class Queue:
    def __init__(self):
        self.start = None
        self.item_count = 0
        
    def is_empty(self):
        return self.start == None
    
    #insert element at end
    def enqueue (self,data):
        n= Node(data)
        if self.is_empty():
            self.start = n
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = n
        self.item_count += 1
    
    #delete at index 0      
    def dequeue(self):
        if not self.is_empty():
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data
        else:
            raise IndexError("Queue Underflow")
    
    #Excess element at front side      
    def get_front(self):
        if not self.is_empty():
            data = self.start.item
            return data
        else:
            raise IndexError("Queue Underflow")
    
    #Excess element at rear side       
    def get_rear(self):
        if not self.is_empty():
            temp = self.start
            while temp.next != None:
                temp = temp.next
            data = temp.item
            return data
        else:
            raise IndexError("Queue Underflow")
        
    def size(self):
        return self.item_count
    
Q1 =Queue()
Q1.enqueue(12)
Q1.enqueue(15)
Q1.enqueue(20)
Q1.enqueue(50)
Q1.enqueue(60)
print("Front element is: ",Q1.get_front())
print("Rear element is: ",Q1.get_rear())
print("Delete element is: ",Q1.dequeue())
Q1.dequeue()
print("Front element is: ",Q1.get_front())
Q1.enqueue(70)
print("Rear element is: ",Q1.get_rear())
            
        
