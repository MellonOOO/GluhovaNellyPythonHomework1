# task 2
phones = {
    "Анна": "+7 900 111-11-11",
    "Иван": "+7 900 222-22-22",
    "Олег": "+7 900 333-33-33"
}
print("введите имя")
name = input(">")
a = 0
for i in phones:
    if i == name:
        a +=1
        print(phones[i])
if a == 0 :
    print("контакт не найден")
    print("напишите номер")
    phon_num = input(">")
    phones[name] = phon_num
for i in phones:
    print(i + ':' + phones[i])





