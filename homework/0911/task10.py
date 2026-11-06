#task 10
order = {
    "number": "A-102",
    "customer": {
        "name": "Максим",
        "email": "max@example.com"
    },
    "items": [
        {"title": "Тетрадь", "price": 80, "quantity": 12},
        {"title": "Ручка", "price": 50, "quantity": 2}
    ],
    "delivery": {
        "method": "курьер",
        "price": 200
    },
    "paid": False,
    "comment": None
}
print(order["number"], order["customer"]["name"])
a = 0
s = 0
for i in order["items"]:
    n =order["items"][a]["quantity"]*order["items"][a]["price"]
    s += n
    print(order["items"][a]["title"],"количество", order["items"][a]["quantity"],"стоимость",order["items"][a]["quantity"]*order["items"][a]["price"] )
    a +=1
if s > 1000:
    order["delivery"]["price"] = 0
order["total"] = s + order["delivery"]["price"]
if order["paid"] == True:
    print("заказ оплачен ")
else:
    print("Ожидает оплаты")
if order["comment"] == None:
    print("комментария нет")


print(order)
