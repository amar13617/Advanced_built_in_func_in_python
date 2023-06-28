def hundred_numbers():
    i = 0
    while i < 100:
        yield i
        i = i+1
    
g = hundred_numbers()
print(next(g))

#Exercise

'''Below you'll find a list containing several tuples full of numbers. 
Use the map function to find the sum of the numbers in each tuple. 
Use manual iteration to print the first two results provided by the resulting map object.'''

numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]
total = map(sum, numbers)
print(next(total))


import itertools

employees = itertools.cycle(["Peter", "Fiona", "Carl", "Helen"])
days = itertools.cycle(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

for day_number in range(1, 31):
    print(f"Day {day_number} ({next(days)}): {next(employees)} closes.")
