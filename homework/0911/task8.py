student = {
    "id": 101,
    "name": "Анна",
    "age": 18,
    "is_active": True,
    "marks": [5, 4, 5, 4],
    "address": {
        "city": "Москва",
        "street": "Лесная"
    },
    "phone": None
}
print(student["name"],student["age"],student["address"]["city"])
student["marks"].append(5)
student["avarage"] = sum(student["marks"])/len(student["marks"])
student["address"]["city"] = "Казань"

print("напишите номер телефона")
phone_num = input(">")
student["phone"] = phone_num
if student["is_active"] == True and student["avarage"] >= 4:
    student["has_scholarship"] = True
else:
    student["has_scholarship"] = False

for i in student:
    print(i, student[i])