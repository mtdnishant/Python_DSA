# Circular Linked List in Python

## 📘 What is a Circular Linked List?

A Circular Linked List is a variation of the standard linked list where the last node points back to the first node, forming a loop. This structure allows for continuous traversal without encountering `NULL`, making it ideal for applications like round-robin scheduling and cyclic buffers.

## 🧱 Node Structure

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
