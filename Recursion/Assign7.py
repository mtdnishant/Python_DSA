## Write a recursive function to calculate sum of first N odd natural numbers

def calSumOdd(n):
    if n == 1:
       return 1
    s = 2 * n - 1 + calSumOdd(n-1)
    return s
sumOdd = calSumOdd(10)
print("odd sum=",sumOdd)