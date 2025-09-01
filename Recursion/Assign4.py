#Q4. Write a recursive function to print first N even natural numbers

def printEven(n):
    if n>0:        
        printEven(n-1)
        print(2 * n,end=' ')
printEven(10)        

###  Write a recursive function to print first N even natural numbers in reverse order.
print("\n")
def printEven(n):
    if n>0:                
        print(2 * n,end=' ')
        printEven(n-1)
printEven(10) 