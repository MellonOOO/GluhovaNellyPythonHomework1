# task 9
numbers = list(map(int, input().split()))
firstNumber = numbers[0]
lastNumber = numbers[-1]
numbers[0] = lastNumber
numbers[-1] = firstNumber
print(numbers)
# task 10
count = numbers[0::2]
print(count)
# task 11
finalList = []
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        finalList.append(numbers[i])
print(f"список чисел, которые больше соседних:{finalList}")
# task 12
reverseList = []
reverseList = (numbers[::-1])
print(f"перевернутый список :{reverseList}")
#task 13
midltList = []
sum = sum(numbers)
count = len(numbers)
midle = sum/count
for i in  numbers:
    if i > midle:
        midltList.append(i)
print(f"числа, которые больше среднего: {midltList}")