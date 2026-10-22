# task 1
numbers = []
n = int(input("введитк число"))
for i  in range(1, n+1) :
    if n >= 0:
        numbers.append(i)
print(numbers)
#task 2
squareList = []
square = 0
for i  in range(0, n+1) :
   square = i ** 2
   squareList.append(square)
print(f"список квадратов чисел из списка:{squareList}")
#task 3
inp = input()
List = []
while inp != "стоп":
    inp = int(inp)
    List.append(inp)
    inp = input()
print(f"количество элементов {len(List)}")
#task 4
for i in List:
    print(i)
#task 5
summ = 0
for i in List:
    summ += i
print(f"сумма всех элементов списка :{summ}")
#task 6
result = 1
for i in List:
    result = result * i
print(f"произведение всех эементов списка = {result}")
#TASK 7
plus = 0
minus = 0
o = 0
for i in List:
    if i == 0:
        o += 1
    elif i > 0:
        plus += 1
    else:
        minus += 1
print(f"количество положительных чисел: {plus}")
print(f"количество отрицательных чисел: {minus}")
print(f"количество нулей: {o}")
#task 8
count = []
for i in List:
    if i%2 == 0:
        count.append(i)
print(f"список четных элементов: {count}")
#task 9
ind = 0
for i  in List :
    if i < 0 :
        List[ind] = 0
        ind += 1
    else:
        ind += 1
print(List)
#task 10
print("впишите новый список в 1 строку через пробел")
Result = []
numbers = list(map(int, input().split()))
summ = sum(numbers)
midle = summ / len(numbers)
for i in numbers:
    if i > midle:
        Result.append(i)
print(f"числа, которые больше среднего: {Result} ")
# task 11
plus = []
minus = []
for i in numbers:
    if i > 0:
        plus.append(i)
    elif i < 0:
        minus.append(i)
print(f"первый положительный элемент - {plus[0]}")
print(f"последний положительный элемент - {plus[-1]}")
print(f"первый отрицательный элемент - {minus[0]}")
print(f"последний отрицательный элемент - {plus[-1]}")
#task 12
for index, value in enumerate(numbers):
    minusInd = index - len(numbers)
    print(f"значение = {value}, неотрицателбный индекс = {index}, отрицвтельный индекс = {minusInd}")
# task 13
n = int(input(" введите допустимое значение индекса"))
for i in numbers:
    if index <= n:
        print(i)
    else:
        print("нет такого индекса")
#task 14
firstNumber = numbers[0]
lastNumber = numbers[-1]
numbers[0] = lastNumber
numbers[-1] = firstNumber
print(numbers)
# task 15
d = len(numbers)
center = 0
if d == 0:
    print("Центра нет")
elif d % 2 == 0:
    print(f"{numbers[d/2]},{numbers[d/2+1]}")
else:
    print(f"{numbers[d/2+0.5]}")
# task 16
reverseList = []
reverseList = (numbers[::-1])
print(f"перевернутый список :{reverseList}")
# task 17
count = numbers[::2]
nonCount = numbers[1:2]
print(f"список четных индексов: {count}")
print(f"список нечетных индексов: {nonCount}")
# task 18
sumList = []
sum = 0
for i in range(1, len(numbers)):
    sum = numbers[i] + numbers[i - 1]
    sumList.append(sum)
print(f"список чисел, которые больше соседних:{sumList}")
# task 19
finalList = []
for i in range(1, len(numbers)-1):
    if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
        finalList.append(numbers[i])
print(f"список чисел, которые больше соседних:{finalList}")
#task 20
st = 0
end = len(numbers)-1
for i in range(0, len(numbers)):
    if st != end:
        if st == end:
            print(f"значениу - {i},индексы - {st}, {end}")
            st += 1
            end -= 1
        else:
            st += 1
            end -= 1
    else:
        print(i)







