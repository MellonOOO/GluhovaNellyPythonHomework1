# task 1
marks = {
    'Ann' : 5,
    'Ivan' : 3,
    'Oleg' : 4,
}
print(marks.get('Ivan'))
marks['Ivan'] = 4
marks['Marya'] = 5
del marks['Oleg']
print(len(marks))
for i in marks:
    print( i, ":", marks[i])


