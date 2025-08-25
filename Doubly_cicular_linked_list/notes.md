# Doubly Circular Linked List (Python)

## Overview
A **Doubly Circular Linked List (CDLL)** is a data structure where each node has pointers to both the previous and next node, and the last node links back to the first, forming a circle. This allows efficient traversal in both directions (forward and backward). :contentReference[oaicite:0]{index=0}

### Common Applications
- Round-robin scheduling  
- Media player playlists  
- Undo/Redo functionality in editors  
- Efficient cache or buffer management  
:contentReference[oaicite:1]{index=1}

---

## Python Implementation (Python ≥ 3.8)

```python
from typing import TypeVar, Generic, Optional, Iterator, Iterable

T = TypeVar("T")

class _Node(Generic[T]):
    __slots__ = ("data", "prev", "next")
    def __init__(self, data: T):
        self.data = data
        self.prev: _Node[T] = self
        self.next: _Node[T] = self
    def __repr__(self):
        return f"_Node({self.data!r})"

class DoublyCircularLinkedList(Generic[T]):
    def __init__(self, iterable: Optional[Iterable[T]] = None):
        self._head: Optional[_Node[T]] = None
        self._size = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def __len__(self) -> int:
        return self._size

    def __bool__(self) -> bool:
        return self._size > 0

    def is_empty(self) -> bool:
        return self._size == 0

    def head(self) -> Optional[T]:
        return None if self._head is None else self._head.data

    def tail(self) -> Optional[T]:
        return None if self._head is None else self._head.prev.data  # type: ignore[union-attr]

    def _insert_between(self, data: T, pred: _Node[T], succ: _Node[T]) -> _Node[T]:
        node = _Node(data)
        node.prev, node.next = pred, succ
        pred.next, succ.prev = node, node
        self._size += 1
        return node

    def _remove_node(self, node: _Node[T]) -> T:
        if self._size == 0:
            raise IndexError("remove from empty list")
        data = node.data
        if self._size == 1:
            self._head = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if node is self._head:
                self._head = node.next
        self._size -= 1
        node.prev = node.next = node  # isolate node
        return data

    def append(self, data: T) -> None:
        if not self._head:
            self._head = _Node(data)
            self._size = 1
        else:
            tail = self._head.prev  # type: ignore[union-attr]
            self._insert_between(data, tail, self._head)

    def prepend(self, data: T) -> None:
        if not self._head:
            self._head = _Node(data)
            self._size = 1
        else:
            tail = self._head.prev  # type: ignore[union-attr]
            self._head = self._insert_between(data, tail, self._head)

    def insert_after(self, node: _Node[T], data: T) -> _Node[T]:
        if self._size == 0:
            raise IndexError("insert_after on empty list")
        return self._insert_between(data, node, node.next)

    def insert_before(self, node: _Node[T], data: T) -> _Node[T]:
        if self._size == 0:
            raise IndexError("insert_before on empty list")
        new_node = self._insert_between(data, node.prev, node)
        if node is self._head:
            self._head = new_node
        return new_node

    def pop_front(self) -> T:
        if not self._head:
            raise IndexError("pop from empty list")
        return self._remove_node(self._head)

    def pop_back(self) -> T:
        if not self._head:
            raise IndexError("pop from empty list")
        return self._remove_node(self._head.prev)  # type: ignore[union-attr]

    def remove_value(self, value: T) -> bool:
        node = self._find_node(value)
        if not node:
            return False
        self._remove_node(node)
        return True

    def clear(self) -> None:
        while self._size:
            self.pop_front()

    def _find_node(self, value: T) -> Optional[_Node[T]]:
        if not self._head:
            return None
        cur = self._head
        for _ in range(self._size):
            if cur.data == value:
                return cur
            cur = cur.next
        return None

    def find(self, value: T) -> Optional[T]:
        node = self._find_node(value)
        return None if node is None else node.data

    def __iter__(self) -> Iterator[T]:
        if not self._head:
            return
            yield
        cur = self._head
        for _ in range(self._size):
            yield cur.data
            cur = cur.next

    def __reversed__(self) -> Iterator[T]:
        if not self._head:
            return
            yield
        cur = self._head.prev  # type: ignore[union-attr]
        for _ in range(self._size):
            yield cur.data
            cur = cur.prev

    def to_list(self) -> list[T]:
        return list(self)

    @classmethod
    def from_iterable(cls, iterable: Iterable[T]):
        return cls(iterable)

    def __str__(self) -> str:
        return "CDLL([" + ", ".join(repr(x) for x in self) + "])"

# Demo usage
if __name__ == "__main__":
    cdll = DoublyCircularLinkedList([1, 2, 3])
    print(cdll)                   # CDLL([1, 2, 3])
    cdll.prepend(0); cdll.append(4)
    print(cdll.to_list())         # [0, 1, 2, 3, 4]
    print(list(reversed(cdll)))   # [4, 3, 2, 1, 0]
    cdll.remove_value(2)
    print(cdll.to_list())         # [0, 1, 3, 4]
    print(cdll.head(), cdll.tail())  # 0 4
    cdll.pop_front(); cdll.pop_back()
    print(cdll.to_list())         # [1, 3]
