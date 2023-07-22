# reduce functions
from functools import reduce

"""
expenses = [("Dinner", 80),
            ("Car repair", 120)
]

for expense in expenses:
    sum = 0
    sum+= expense[1]
    print(sum)


"""


#the reduce function in practice 
#imported the reduce function on top


expenses = [("Dinner", 80),
            ("Car repair", 120)
            ("Towing", 40)
]

sum = reduce(lambda a,b: a[1] + b[1], expenses)
print(sum)