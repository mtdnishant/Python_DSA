## Write a recursive function to calculate sum of first N Even natural numbers

def calSumEven(n):
    if n == 2:
       return 2
    s = 2 * n + calSumEven(n-1)
    return s
sumOdd = calSumEven(10)
print("Even sum=",sumOdd)