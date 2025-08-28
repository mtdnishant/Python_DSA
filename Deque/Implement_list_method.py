class Deque:
    def __init__(self):
        self.item =[]
    
    #Check node is empty or not    
    def is_empty(self):
        return len(self.item) == 0
    
    #insert method at front
    def insert_front(self,data):
        self.item.append(data)
    
    #insert method at rear      
    def insert_rear(self,data):
        self.item.insert(0,data)
    
    #delete method at front       
    def delete_front(self):
        if not self.is_empty():
            self.item.pop()
        else:
            raise IndexError("Deque is Underflow")
    
     #delete method at rear       
    def delete_rear(self):
        if not self.is_empty():
            self.item.pop(0)
        else:
            raise IndexError("Deque is Underflow")
    
    #Excess element at front side  
    def get_front(self):
        return self.item[-1]
    
    #Excess element at rear side   
    def get_rear(self):
        return self.item[0]
    
    def size(self):
        return len(self.item)
    
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
print("Front element is:",d1.get_front())  #6
print("Rear element is: ",d1.get_rear())   #8

        