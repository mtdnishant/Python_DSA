#####  Priority queue ###
class PriorityQueue:
    def __init__(self):
        self.item = []
    
    #insert element According to priority
    def push(self,data,priority):
        idx = 0
        while idx<len(self.item) and self.item[idx][1] <=priority:
            idx+=1
        self.item.insert(idx,(data,priority))
    #Pop method   
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty...")
        else:
            return self.item.pop(0)[0]

    def is_empty(self):
        return len(self.item) == 0    
     
    def size(self):
        return len(self.item)
  
PQ = PriorityQueue()
PQ.push("Amit",4)
PQ.push("Arjun",7)
PQ.push("Ashima",2)
PQ.push("Agrah",5)
PQ.push("Anant",8)
PQ.push("Ambika",1)
print("priority rank:")
while not PQ.is_empty():
    print(PQ.pop())
