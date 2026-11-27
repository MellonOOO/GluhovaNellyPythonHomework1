"""#task 1
s = input(">").split()
print(f"меня зовут {s[0]}, мне лет {s[1]}")
# task 2
s = input(">").split()
print(f" Имя : {s[0]}\n Город : {s[1]}\n Любимый предмет : {s[2]}")
# task 3
s = input(">").split()
print(f"{s[0]} + {s[1]} = {int(s[0])+int(s[1])}\n{s[0]} - {s[1]} = {int(s[0])-int(s[1])}\n{s[0]} * {s[1]} = {int(s[0])*int(s[1])}\n{s[0]} / {s[1]} = {(int(s[0])/int(s[1])):.2f}")
# task 4
s = input(">").split()
print(f"Товар : {s[0]}. Цена : {int(s[1]):.2f}.")
# task 5
s = list(map(int,input(">").split()))
print(f"{(sum(s)/len(s)):.2f}")
#task 6
s = int(input(">"))
print(f"{s:.1f} °C = {(s * 9/5 + 32):.1f} °F")
# task 7
s = input(">").split()
print(f"{s[0]}: {s[2]} шт. x {(int(s[1])):.2f} руб. = {(int(s[1])*int(s[2])):.2f} руб.")
# task 8
s = list(map(int,input(">").split()))
print(f"исходная цена : {(s[0]):.2f} руб. размер скидки : {(s[0]/100*s[1]):.2f} руб. итого : {(s[0]-s[0]/100*s[1]):.2f} руб.")
# task 9
s = list(map(int,input(">").split()))
print(f"{(s[0]/s[1]*100):.1f}%")
# task 10
s = input("введите номер заказа от `0` до `999999` >")
print(f"Заказ №{s.rjust(6, "0")}")
# task 11
s = input(">").split()
print(f"{s[0].rjust(2, "0")}:{s[1].rjust(2, "0")}:{s[2].rjust(2, "0")}")
# task 12
s = input(">").split()
print(f"{s[0]}: {(int(s[1])):+.2f} сек.")
# task 13
s = input(">")
print(f"|{s.ljust(20, " ")}|\n|{s.center(20, " ")}|\n|{s.rjust(20, " ")}|")
# task 14
s = input(">")
print(f"{s.center(30,"=")}")
# task 15
s = input(">").split()
a = str(round(float(s[1]), 2))
print(f"{s[0].ljust(20)}{a.rjust(10)}")
# tassk 16
names = input("введите названия>").split()
costs = input("введите цены>").split()
print(f"Товар                     Цена")
for i in range(0, len(names)):
    print(f"{names[i].ljust(20)}{str(round(float(costs[i]),2)).rjust(10)}")
# task 17
s = int(input(">"))
print(f"{s:,}")
# task 18
s = int(input(">"))
print(f"Десятичная: {s}\nДвоичная: {s:b}\nШестнадцатеричная: {s:x}")
# task 19
summ = 0
name = input("названия>").split()
cost = input("цены>").split()
count = input("количества>").split()
print(f"{"Товар".ljust(16)}{"количество".ljust(16)}{"цена за штуку".ljust(16)}{"стоимость позиц.".center(16)}")
for i in range(0, len(name)):
    summ += float(cost[i])*int(count[i])
    print(f"{name[i].ljust(16)}{(count[i]).ljust(16)}{str(round(float(cost[i]),2)).ljust(16)}{str(round(int(count[i])*float(cost[i]),2))}")
print(f"итого: {summ:.2f}")
# task 20
n = int(input(">"))
print(f"{"число".rjust(10)}{"квадрат".rjust(10)}{"куб".rjust(10)}")
for i in range(1, n+1):
    print(f"{str(i).rjust(10)}{str(i**2).rjust(10)}{str(i**3).rjust(10)}")
"""







