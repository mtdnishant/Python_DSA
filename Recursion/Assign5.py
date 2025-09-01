### Write a recursive function to print first N square natural numbers.

def calSquare(n):
    if n> 0:
        calSquare(n-1)
        print(n * n,end=' ')
print("First N Squares...")
calSquare(10)    