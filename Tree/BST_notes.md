# Binary Search Tree (BST)

## 1. Definition

A **Binary Search Tree (BST)** is a node-based data structure that satisfies:
- For any node `X`, all keys in its left subtree are **less than** `X`'s key.
- All keys in its right subtree are **greater than** `X`'s key.  
:contentReference[oaicite:0]{index=0}

Each node typically contains:
- A **key** (unique identifier)
- Optional **value** or data
- Pointer/reference to **left child**
- Pointer/reference to **right child**
- (Optional) Pointer to **parent node** or additional metadata  
:contentReference[oaicite:1]{index=1}

## 2. Properties & Terminology

- **Root**: The topmost node of the tree (has no parent).
- **Leaf**: Node with no children.
- **Subtree**: A node and all of its descendants.
- **Height**: Maximum number of edges from node to its deepest leaf.
- **Depth**: Number of edges from node to the root.  
:contentReference[oaicite:2]{index=2}

In-order traversal of a BST yields sorted order of keys.  
:contentReference[oaicite:3]{index=3}

## 3. Core Operations

- **Search**: Traverse left or right based on comparison until finding the key or reaching `None`.  
- **Insert**: Place a new leaf node in proper position to maintain BST property.
- **Delete**: Three cases:
  1. **Leaf**: Remove directly.
  2. **One child**: Replace node with its child.
  3. **Two children**: Replace node’s key with **in-order successor** (smallest in right subtree) or **in-order predecessor** (largest in left subtree), then delete that node.  
    :contentReference[oaicite:4]{index=4}

These operations run in `O(h)` time, where *h* is the tree height. In balanced BSTs, that’s `O(log n)`; in worst-case (like a skewed tree), it's `O(n)`.  
:contentReference[oaicite:5]{index=5}

## 4. Example Python Implementation

```python
class Node:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, key, value=None):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if node is None:
            return Node(key, value)
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value  # Update existing key
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        return (self._inorder(node.left) if node.left else []) + \
               [(node.key, node.value)] + \
               (self._inorder(node.right) if node.right else []) if node else []

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Two children: use in-order successor
            succ = self._min_node(node.right)
            node.key, node.value = succ.key, succ.value
            node.right = self._delete(node.right, succ.key)
        return node

    def _min_node(self, node):
        while node.left:
            node = node.left
        return node
