# Recursion

def factorial(n):
    if n == 1: return 1        #base case(so that the recursion can stop)
    return n * factorial(n-1)  #recursive case
    
print(factorial(3))
print(factorial(4))
