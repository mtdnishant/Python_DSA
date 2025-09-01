###    Write a recursive function to print first N odd natural numbers.

def printOdd(n):
    if n>0:        
        printOdd(n-1)
        print(2 * n - 1,end=' ')
printOdd(10)        

# Write a recursive function to print first N odd natural numbers in reverse order.

def printOdd(n):
    if n>0:        
        print(2 * n - 1,end=' ')
        printOdd(n-1)
printOdd(10)        