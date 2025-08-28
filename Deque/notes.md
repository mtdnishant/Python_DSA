# Python `deque` (Double-Ended Queue)

A **deque** (pronounced *deck*) — or **double-ended queue** — is a versatile data structure that allows insertion and deletion from **both ends**, offering **O(1)** performance for these operations.  
It generalizes both **stack** (LIFO) and **queue** (FIFO) behaviors. :contentReference[oaicite:0]{index=0}

---

##  Why Use `deque` Over `list`?

- Efficient operations at **both ends**: `append`, `appendleft`, `pop`, `popleft` are all **O(1)**. Lists, by contrast, are O(n) for front-end insertions or deletions. :contentReference[oaicite:1]{index=1}  
- **Thread-safe** operations: append and pop from both ends are safe for use across threads without explicit locking. :contentReference[oaicite:2]{index=2}  
- Supports optional **maximum length (`maxlen`)**: acts as a bounded buffer—new inserts automatically discard items from the opposite end if full. :contentReference[oaicite:3]{index=3}

---

##  Basic Usage

```python
from collections import deque

dq = deque([1, 2, 3])         # Initialize from iterable
dq2 = deque(maxlen=3)         # Bounded deque

dq.append(4)                  # Add to right end → deque([1,2,3,4])
dq.appendleft(0)              # Add to left end → deque([0,1,2,3,4])
dq.pop()                      # Remove from right → 4
dq.popleft()                  # Remove from left → 0
