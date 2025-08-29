######## Queue by list method ########
class Queue:
    def __init__(self):
        self.item =[]
        
    def is_empty(self):
        return len(self.item) == 0
    
    #insert element at end
    def enqueue (self, data):
        self.item.append(data)
    
    #delete at index 0    
    def dequeue (self):
        if not self.is_empty():
            return self.item.pop(0)
        else:
            raise IndexError("Queue Underflow")
    
    #Excess element at front side     
    def get_front(self):
        if not self.is_empty():
            return self.item[0]
        else:
            raise IndexError("Queue  Underflow")
    
    #Excess element at rear side       
    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("Queue  Underflow")
    
    def size (self):
        return len(self.item)
    
Q1 =Queue()
Q1.enqueue(12)
Q1.enqueue(15)
Q1.enqueue(20)
Q1.enqueue(50)
Q1.enqueue(60)
print("Front element is: ",Q1.get_front())
print("Rear element is: ",Q1.get_rear())
print("Delete element is: ",Q1.dequeue())
print("After dequeue front element is: ",Q1.get_front())
                  