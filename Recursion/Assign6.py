# Write a recursive function to calculate sum of first N natural numbers.

def calSum(n):
    if n == 1:
        return 1
    s = n + calSum(n-1)
    return s

sum = calSum(10)
print("sum=",sum)