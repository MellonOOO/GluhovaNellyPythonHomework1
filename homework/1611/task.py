import string
""""# task 1
s = input(">")
print(ord(s))
# task 2
s = input(">")
ss = input(">")
if ord(s) > ord(ss):
    print(ord(s)-ord(ss))
else:
    print(ord(ss)-ord(s))
# task 3
english_letters = "abcdefghijklmnopqrstuvwxyz"
s = input("введите предложение>")
n =int (input("введите сдвиг>"))
out = ""
for i in s:
    if i in english_letters:
        first_let = english_letters.index(i)
        final_let = (first_let + n) % len(english_letters)
        out += english_letters[final_let]
    else:
        out += " "
print(out)
# task 4
english_letters = "abcdefghijklmnopqrstuvwxyz"
english_letters += english_letters.upper()
e_l_num = 0
num = "1234567890"
num_num = 0
pun = string.punctuation
pun_num = 0
el_num = 0
s = input(">")
for i in s:
    if i in english_letters:
        e_l_num += 1
    elif i in num:
        num_num += 1
    elif i in pun:
        pun_num += 1
    else:
        el_num += 1
print("английские буквы -", e_l_num, "цифры -", num_num, "знаки препинания -", pun_num, "другое -", el_num)

# task 5
english_letters = "abcdefghijklmnopqrstuvwxyz"
e_l_num = 0
up_english_letters = english_letters.upper()
up_e_l_num = 0
num = "1234567890"
num_num = 0
pun = string.punctuation
pun_num = 0
s = input("введите пароль>")
for i in s:
    if i in english_letters:
        e_l_num += 1
    elif i in num:
        num_num += 1
    elif i in pun:
        pun_num += 1
    elif i in up_english_letters:
        up_e_l_num += 1
if e_l_num > 1 and num_num > 1 and pun_num > 1 and up_e_l_num > 1 and len(s) >= 8:
    print("пароль подходит")
else:
    print("пароль не подходит")
# task 6
out = ""
s = input(">")
s = s.lower()
english_letters = "abcdefghijklmnopqrstuvwxyz"
for i in english_letters:
    if i not in s:
        out += i
print(out)
# task 7
s = input(">")
s = s.strip()
print(s)
# task 8
s = input(">")
s = s.lower()
ss =""
for i in s:
    if i in string.punctuation:
        ss += ""
    elif i == " ":
        ss += ""
    else:
        ss += i
reverst_ss = ss[::-1]
a = 0
if reverst_ss == ss:
    print("да")
else:
    print("нет")
    """
# task 9
s = input(">")
l = list(s)
unig_letters = []
out =""
for i in l :
    if i not in unig_letters:
        unig_letters.append(i)
for i in unig_letters:
    out += i + str(s.count(i))
print(out)