###   Priority queue implementation linked list method

class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item =item
        self.priority=priority
        self.next=next
    
class PriorityQueue:
    def __init__(self):
        self.start=None
        self.item_count = 0
        
    def is_empty(self):
        return self.start == None
    #check priority after insert 
    def push(self,data,priority):        
        n =Node(data,priority)
        if not self.start or priority < self.start.priority:
            n.next=self.start
            self.start = n
        else:
            temp = self.start
            while temp.next and temp.next.priority <=priority:
                temp =temp.next
            n.next = temp.next
            temp.next = n
        self.item_count +=1
        
    #Pop method
    def pop(self):
        if not self.is_empty():
            data = self.start.item
            self.start =self.start.next
            self.item_count -=1
            return data
        else:
            raise IndexError("Priority Queue is empty...")    

PQ =PriorityQueue()
PQ.push("Amit",4)
PQ.push("Arjun",7)
PQ.push("Ashima",2)
PQ.push("Agrah",5)
PQ.push("Anant",8)
PQ.push("Ambika",1)
print("priority rank:")
while not PQ.is_empty():
    print(PQ.pop())                