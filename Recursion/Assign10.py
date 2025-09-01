## Write a recursive function to calculate sum of squares of first N natural numbers.

def calSumSq(n):
    if n== 1:
        return 1
    return n * n +calSumSq(n-1)

sqSum = calSumSq(5)
print("N no square sum:",sqSum)
    