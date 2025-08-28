class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next
        
class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
        
    #Check node is empty or not    
    def is_empty(self):
        return self.item_count == 0
    
    #insert method at front
    def insert_front(self,data):
        n = Node(data,None,self.front)
        if self.is_empty():
            self.rear = n            
        else:
            self.front.prev = n
        self.front=n
        self.item_count +=1
    
    #insert method at rear     
    def insert_rear(self,data):
        n = Node(data,self.rear)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next =n
        self.rear = n
        self.item_count += 1
    
    #delete method at front   
    def delete_front(self):
        if self.is_empty():
            raise IndexError ("Deque is Underflow")
        elif self.front ==self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev=None
        self.item_count -=1
     
    #delete method at rear   
    def delete_rear(self):
        if self.is_empty():
            raise IndexError ("Deque is Underflow")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None             
        self.item_count -= 1
    #Excess element at front side  
    def get_front(self):
        if self.is_empty():
            raise IndexError ("Deque is Underflow")
        else:
            return self.front.item      
    #Excess element at rear side      
    def get_rear(self):
        if self.is_empty():
            raise IndexError ("Deque is Underflow")
        else:
            if self.rear.next == None:
                data = self.rear.item
                return data
    #get Deque size
    def size(self):
        return self.item_count
            
d1 = Deque()
d1.insert_front(4)
d1.insert_front(6)
d1.insert_rear(8)
d1.insert_rear(2)
d1.insert_front(10)
print("Front element is:",d1.get_front())  #10
print("Rear element is: ",d1.get_rear())   #2
d1.delete_front()
d1.delete_rear()
print("After delete front element is:",d1.get_front())  #6
print("After delete rear element is: ",d1.get_rear())   #8                  
            