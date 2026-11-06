#task9
product = {
    "id": 42,
    "title": "Наушники",
    "price": 3500,
    "in_stock": True,
    "tags": ["техника", "звук"],
    "specs": {
        "wireless": True,
        "battery_hours": 30,
        "color": "чёрный"
    },
    "reviews": [
        {"author": "Иван", "rating": 5, "text": "Хороший звук"},
        {"author": "Ольга", "rating": 4, "text": "Удобные"}
    ]
}
print(product["title"], product["price"], product["specs"]["color"], product["specs"]["battery_hours"])
rebate = 10 # скидка
product["price"] = product["price"]/100*(100-rebate)
product["tags"].append("скидка")
product["reviews"].append({"author": "Анна", "rating": 3, "text": "Быстро разряжаются"})

ratings = [review['rating'] for review in product['reviews']]
average_rating = sum(ratings) / len(ratings)
product["rating"] = average_rating
a = 0
for i in ratings:
    if i < 4:
        print(product["reviews"][a]["author"])
        a += 1
    else:
        a += 1
if product["in_stock"] == True and product["specs"]["wireless"] == True:
    print("можно заказать")
else:
    print("не подходит")
