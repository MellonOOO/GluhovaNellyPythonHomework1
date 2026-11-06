#task7
journal = {
    "Анна": [5, 4, 5],
    "Иван": [3, 4, 3],
    "Олег": [4, 5, 4],
    "Мария": []
}
mid = 0
mid_jour = {}
for i in journal:
    if len(journal[i]) != 0:
        mid = sum(journal[i])/len(journal[i])
        mid = round(mid, 2)
        mid_jour[i] = mid
    else:
       print(i," : ","нет оценок")
for i in mid_jour:
    if mid_jour[i] >= 4:
        print(i)
# 5 часть . что нужно сделать?
# максимальная средняя оценка = 5
max_mark = 5
a = 0
for i in mid_jour:
    if mid_jour[i] == 5:
        print(i)
        a += 1
if a == 0:
    print("нет данных")
# максимальная среди студентов
max_mark = 0
max_name = ""
for i in mid_jour:
    if mid_jour[i] > max_mark:
        max_mark = mid_jour[i]
        max_name = i
print(max_name)
