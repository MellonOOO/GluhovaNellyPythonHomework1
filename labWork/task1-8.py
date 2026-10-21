# Gluhova Nelly
# task 1

numbers = list(map(int, input().split()))
for i in numbers:
    print(i)
# task 2
sum = int(0)
for i in numbers:
    sum += i
print(f"сумма всех элементов списка = {sum}")
# task 3
plus = 0
for i in numbers:
    if i > 0 :
        plus += 1
print(f"количество положительных чисел = {plus}")
# task 4
count = []
for i in numbers:
    if i % 2 == 0 :
        count.append(i)
print(f"список четных чисел : {count}")
# task 5
max = -10000000000
for i in numbers:
    if i > max:
        max = i
print(f"наибольшее число в списке - {max}")
# task 6
index = 0
num = int(input("введите число"))
for i in numbers:
    if i != num:
        index += 1
    else:
        print(f"индекс заданного числа = {index}")
        index += 1
# task 7
num = int(input("введите число"))
countOfNum = 0
for i in numbers:
        if i == num:
            countOfNum += 1
print(f"количество чисел, равных заданному = {countOfNum}")
# task 8
index = 0
for i in numbers:
        if i < 0:
            numbers[index] = 0
            index += 1
        else:
            index += 1
print(numbers)