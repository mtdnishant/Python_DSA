# Stack in Python

A **stack** is an Abstract Data Type (ADT) that adheres to **LIFO** (Last-In, First-Out) principle—elements are added and removed only from the *top*. Key operations typically include:

- `push(x)`: Add element `x` to the top  
- `pop()`: Remove and return the top element  
- `peek()` / `top()`: Return the top element without removal  
- `is_empty()`: Check if stack is empty  
- `size()`: Return number of elements  

You can implement stacks in Python using:
- Lists (`.append()` / `.pop()` at end)  
- `collections.deque`  
- Thread-safe `queue.LifoQueue`  
- Custom class (via list or linked list)  
:contentReference[oaicite:0]{index=0}

---

##  Why Use a Stack?

- Implements nested control flow, e.g., the function call stack  
- Supports algorithms like depth-first search, backtracking, expression parsing  
- Enables features like undo/redo, browser history  
:contentReference[oaicite:1]{index=1}

---

##  Python Implementations

### 1. Using a Python List

```python
stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')

# Peek
top = stack[-1] if stack else None

# Pop
elem = stack.pop() if stack else None
