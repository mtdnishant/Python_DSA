# Doubly Linked List in Python

A **doubly linked list (DLL)** is a data structure where each node contains:
- A **data field**
- A **pointer to the next node** (`next`)
- A **pointer to the previous node** (`prev`)

This structure allows efficient two-way traversal.  
:contentReference[oaicite:0]{index=0}

---

## 1. Node Structure

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

