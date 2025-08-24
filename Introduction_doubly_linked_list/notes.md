# Doubly Linked List

## 1. Definition
A **doubly linked list** is a linear data structure where each node contains:
- A `data` field,
- A `prev` pointer/reference to the previous node,
- A `next` pointer/reference to the next node :contentReference[oaicite:2]{index=2}.

The `prev` of the first node and the `next` of the last node typically point to `null` (or a sentinel) :contentReference[oaicite:3]{index=3}.

## 2. Advantages
- Can traverse **both forwards and backwards** easily :contentReference[oaicite:4]{index=4}.
- **Efficient insertion and deletion**, especially if the node to be manipulated is known—no need to traverse the list to find the previous node :contentReference[oaicite:5]{index=5}.

## 3. Disadvantages
- **More memory overhead**: each node needs an extra pointer (prev) :contentReference[oaicite:6]{index=6}.
- **Pointer operations are more complex**: insertion/deletion involves updating multiple pointers carefully :contentReference[oaicite:7]{index=7}.

## 4. Node Structure Examples

### In C++
```cpp
struct Node {
    int data;
    Node* prev;
    Node* next;

    Node(int d) : data(d), prev(nullptr), next(nullptr) {}
};
