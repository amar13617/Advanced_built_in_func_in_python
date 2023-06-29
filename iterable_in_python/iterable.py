students = [
    {"name":"Rolf", "grades": (9,82,83,88)},
    {"name":"Rolv", "grades": (99,57,24,88)},
    {"name":"Anna", "grades": (91,88,80,88)},
    {"name":"Andrew", "grades": (22,72,73,48)}
]

list = []
for student in students:
    list.append(student['grades'])

print(map(next(list)))