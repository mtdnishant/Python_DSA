####   Write a recursive function to print first N natural numbers.

def printN(n):
    if n == 1:
        print(n)
        return 1
    a = 1 + printN(n-1)
    print(a)
    return a
    
N = printN(10)


### Another method
def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=' ')

printN(10)