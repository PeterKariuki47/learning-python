# filter functions

numbers = [1,2,3,4,5,6,7,8]

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False 

result = filter(isEven, numbers)
print(list(result))

# Modified code using a lambda function

numbers = [11,12,13,14,15,16,17,18,19]

result= filter(lambda n:n%2==0, numbers)
print(list(result))