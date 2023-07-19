#Nested functions

def count():
    count = 0

    def increment():
        nonlocal count # the keyword "nonlocal" is used to call a variable that is outside the function but in another function
        count = count + 1
        print(count)
    increment()

count() 

