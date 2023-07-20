# filter functions

numbers = [1,2,3,4,5,6,7,8]

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

result = filter(isEven, numbers)
print(list(result))