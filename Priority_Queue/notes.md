# Priority Queue

A **Priority Queue** is an *abstract data type* (ADT) that stores elements each associated with a **priority**. Unlike a regular queue (FIFO), elements are dequeued based on their priority—*the highest (or lowest) priority element is served first* :contentReference[oaicite:0]{index=0}.

---

##  Operations

A priority queue typically supports:

- **Insert** (`insert`, `enqueue`): Add an element with an associated priority :contentReference[oaicite:1]{index=1}.
- **Peek / Find**: Retrieve (but do not remove) the highest-priority element:
  - `maximum` in a *max-priority* queue
  - `minimum` in a *min-priority* queue :contentReference[oaicite:2]{index=2}.
- **Extract** (`extract_max`, `extract_min`): Remove and return the top-priority element :contentReference[oaicite:3]{index=3}.
- **Priority Update** (optional): Change an element’s priority using operations like `increase_key` or `decrease_key` :contentReference[oaicite:4]{index=4}.

---

##  Implementations & Performance

### 1. Unsorted Array
- **Insert**: O(1) – just append.
- **Extract**: O(n) – search for highest/lowest priority :contentReference[oaicite:5]{index=5}.

### 2. Sorted Array
- **Insert**: O(n) – maintain order on insertion.
- **Extract**: O(1) – remove first (or last) element :contentReference[oaicite:6]{index=6}.

### 3. Linked List
- **Insert**: O(n) – find correct position if ordered.
- **Extract**: O(1) – or O(n) for unordered lists :contentReference[oaicite:7]{index=7}.

### 4. Heap (Binary Heap)
- Most efficient common implementation:
  - **Insert**: O(log n)
  - **Extract**: O(log n)
  - **Peek**: O(1) :contentReference[oaicite:8]{index=8}.

### 5. Others (BST, Bucket Queue)
- **Balanced BST**: O(log n) for insert and extract :contentReference[oaicite:9]{index=9}.
- **Bucket Queue** (for integer-limited priorities): O(1) insert and delete (ideal when priority range is small) :contentReference[oaicite:10]{index=10}.

---

##  Comparison of Implementations

| Implementation     | Insert        | Extract (Max/Min) | Peek       |
|--------------------|---------------|-------------------|------------|
| Unsorted Array     | O(1)          | O(n)              | O(n)       |
| Sorted Array       | O(n)          | O(1)              | O(1)       |
| Linked List        | O(n)          | O(1) or O(n)      | O(1) or O(n) |
| Binary Heap        | O(log n)      | O(log n)          | O(1)       |
| Balanced BST       | O(log n)      | O(log n)          | O(log n)   |
| Bucket Queue       | O(1)          | O(1) (avg)        | O(1)       |

---

##  Real-World Examples & Applications

Think of how **emergency rooms** triage patients: critical cases are served before less urgent ones—this is priority queue behavior:contentReference[oaicite:11]{index=11}.

Priority queues are essential in many algorithms, including:

- **Dijkstra’s shortest-path algorithm** (min-priority queue) :contentReference[oaicite:12]{index=12}.
- **Prim’s minimum spanning tree** algorithm :contentReference[oaicite:13]{index=13}.
- **Huffman coding** for data compression :contentReference[oaicite:14]{index=14}.
- **Event-driven simulations**, like scheduling by time :contentReference[oaicite:15]{index=15}.

---

##  Language Support & Library Examples

- **Java**: `java.util.PriorityQueue` uses a binary heap under the hood. Elements are ordered by natural ordering or a provided `Comparator` :contentReference[oaicite:16]{index=16}.
- **C++**: `std::priority_queue` (in `<queue>`) provides O(1) access to top, with O(log n) insertion/extraction. Custom comparison functions are supported :contentReference[oaicite:17]{index=17}.
- **Python**: Use the built-in `PriorityQueue` class (thread-safe) or the `heapq` module for heap-based priority queues :contentReference[oaicite:18]{index=18}.

---

##  Summary

- A **Priority Queue** is an abstract data type where each element has a priority, and the highest (or lowest) priority element is retrieved first.
- It supports operations like insert, peek, extract, and optional priority updates.
- The **binary heap** is the most efficient and commonly used implementation, offering O(log n) inserts and removals.
- Widely used in graph algorithms, data compression, simulations, and system task scheduling.
- Available in standard libraries across major programming languages such as Java, C++, and Python.

---

Let me know if you'd like code examples (in Markdown) for specific languages like Java, Python, or C++, or if you'd like to expand the documentation (e.g., include diagrams or pseudocode).
::contentReference[oaicite:19]{index=19}
