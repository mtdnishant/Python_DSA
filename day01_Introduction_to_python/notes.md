
---

```markdown
# Singly Linked List (SLL)

## 🔹 What is a Singly Linked List?
A **Singly Linked List (SLL)** is a type of **linear data structure** where elements (called **nodes**) are connected using **links (pointers)**.  
Unlike arrays, elements are **not stored in contiguous memory**, but each node points to the **next node** in the sequence.  

---

## 🔹 Structure of a Node
Each node in a singly linked list has two parts:
1. **Data** → Stores the actual value.  
2. **Next (Pointer)** → Stores the address (reference) of the next node.  

The last node’s **next** pointer is `NULL` (or `None` in Python), which indicates the **end of the list**.

**Diagram:**
```

Head → \[Data | Next] → \[Data | Next] → \[Data | Next] → NULL

````

---

## 🔹 Important Terms
- **Head** → Pointer that stores the address of the first node.  
- **Node** → An element of the list.  
- **NULL (None)** → Represents the end of the list.  

---

## 🔹 Advantages of Singly Linked List
1. **Dynamic size** → Can grow/shrink at runtime.  
2. **Efficient insert/delete** → Insertion and deletion are faster than arrays (no shifting needed).  
3. **Memory utilization** → Memory is allocated as needed.  

---

## 🔹 Disadvantages
1. **No backward traversal** → You can only move forward (one direction).  
2. **Extra memory** → Each node stores an extra pointer.  
3. **Access is sequential** → To access the ith element, you must start from the head and move one by one.  

---

## 🔹 Operations on Singly Linked List
1. **Traversal** → Visiting each node from head to tail.  
2. **Insertion**
   - At beginning  
   - At end  
   - At specific position  
3. **Deletion**
   - From beginning  
   - From end  
   - From specific position  
4. **Search** → Find if a value exists.  
5. **Update** → Modify node data.  

---

## 🔹 Example in Python
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # initially no link

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Display the list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("NULL")

# Usage
sll = SinglyLinkedList()
sll.insert(10)
sll.insert(20)
sll.insert(30)
sll.display()
````

**Output:**

```
10 → 20 → 30 → NULL
```

---

✅ **In short:**
A **Singly Linked List** is a chain of nodes where each node contains data and a reference to the next node. It is useful when you need dynamic memory and frequent insertions/deletions.

```

