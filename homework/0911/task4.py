#task4
marks = {
    "Анна": 5,
    "Иван": 3,
    "Олег": 4,
    "Мария": 5,
    "Пётр": 2
}
sum = 0
for i in marks:
    sum += marks[i]
if len(marks) != 0:
    midle = sum / len(marks)
    print("средняя оценка группы:",midle)
    print("студенты с оценкой 5:")
    for i in marks:
        if marks[i] == 5:
            print(i)
    count = 0
    for i in marks:
        if marks[i] < 4:
            count += 1
    print("количество студентов с оценкой ниже 4:", count)
    good_marks = {}
    for i in marks:
        if marks[i] >= 4:
            good_marks[i] = marks[i]
    print(good_marks)

else:
    print("нет данных")
