# Recursion in Python

> A concise, practical guide with patterns, pitfalls, and examples.

## What is Recursion?  
Recursion is a technique where a function calls itself to solve a problem by breaking it into smaller subproblems (same form).

**Two must-haves:**  
1. **Base case** – stopping condition  
2. **Progress** – each recursive call moves toward that base

---

## Examples

### 1) Factorial (single recursion)
```python
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("n must be >= 0")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)
