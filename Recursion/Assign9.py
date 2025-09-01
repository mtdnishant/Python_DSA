##  Write a recursive function to calculate factorial of a number.

def calFact(n):
    if n==1:
        return 1
    return n * calFact(n-1)

fact = calFact(7)
print("factorial=",fact)
