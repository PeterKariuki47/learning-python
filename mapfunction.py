#Map functions

numbers = [1,2,3,4]

def double(a):
    return a*2

result=map(double,numbers)
print(list(result))


#simplifying the code using a lambda function

numbers = [1,2,3,4,5]

result = map(lambda a:a*2, numbers)
print(list(result))