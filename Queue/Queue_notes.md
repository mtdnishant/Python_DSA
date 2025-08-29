# Python Queue (Queue Data Structure) 

Yeh file Python mein Queue data structure ka overview aur examples provide karti hai, including single-threaded, threaded, aur async use cases.

---

##  1. Queue kya hai?

**Queue** ek linear data structure hai jo elements ko **FIFO** (First-In, First-Out) order mein process karta hai.

---

## 2. `collections.deque` ka use (fast & simple)

```python
from collections import deque

q = deque()
q.append("apple")       # enqueue
q.append("banana")
first_item = q.popleft()  # dequeue → "apple"
print(first_item, list(q))  # apple ['banana']
