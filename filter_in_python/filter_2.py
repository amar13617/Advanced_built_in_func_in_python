numbers = [23,33,22,34]

def filter_even(value):
    if value % 2 == 0:
        return True
    
filter_object = filter(filter_even, numbers)
#print(next(filter_object))
#print(next(filter_object))
print(list(filter_object))
