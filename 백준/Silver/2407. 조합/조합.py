def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
n, m = map(int, input().split())
from fractions import Fraction
  
def combination(n, m):
    return Fraction(factorial(n), (factorial(m)*factorial(n-m)))

print(int(combination(n,m)))