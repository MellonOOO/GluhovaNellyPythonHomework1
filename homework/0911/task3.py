#task3
prices = {
    "хлеб": 50,
    "молоко": 90,
    "сыр": 150,
    "яблоко": 30
}
print("напишите название товара")
name = input(">")
print("напишите количество товара")
num = int(input(">"))
if name in prices:
    for i in prices:
        if name == i:
            cost = prices[i]
            and_cost = cost * num
    print("стоймость покупки: ", and_cost)
else:
    print("товар не найден")
print("товары с ценой больше 100 рублей:")
for i in prices:
    if prices[i] > 100:
        print(i)


