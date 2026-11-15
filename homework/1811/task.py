import string
# task 1
s = input(">")
print(s.title())
# task 2
s = input(">")
print(s.upper())
# task3
s = input(">")
print(s.strip())
# task 4
s = input(">")
print(s.replace(" ", "_"))
# task 5
s = input(">")
print(s.count("a"))
# task 6
s = input("введите предложение >")
word = input("введите слово >")
print(word in s)
# task 7
s = input(">")
s = s.split(".")
word = "txt"
print(word in s)
# task 8
vowels = "ауоыияюэеёАЁУЕЭЮИОЯЫ"
s = input(">")
count = 0
for i in s:
    if i in vowels:
        count += 1
print(count)
# task 9
num = "1234567890"
s = input(">")
count = 0
for i in s:
    if i in num:
        count += 1
print(count)
# task 10
s = input(">")
l = s.split()
print(len(l))
# task 11
long = 0
longest_word = ""
s = input(">")
l = s.split()
for i in l:
    if len(i) > long:
        long = len(i)
        longest_word = i
print(longest_word)
# task 12
# срез
s = input(">")
c = s[::-1]
print(c)
# цикл
c = ""
for i in s:
    c = i + c
print(c)
# task 13
s = input("введите строку>")
word = input("введите символ>")
c = ""
for i in s:
    if i == word:
        c += ""
    else:
        c += i
print(c)
# task 14
s = input(">")
c = ""
n = 0
for i in s:
    if n % 2 == 0:
        c += i.upper()
        n += 1
    else:
        c += i.lower()
        n += 1
print(c)
# task 15
s = input(">")
s = s.lower()
s = s.replace(" ", "")
c = s[::-1]
a = 0
for i in range(len(s)):
    if s[i] != c[i]:
        a += 1
if a == 0:
    print(True)
else:
    print(False)
# task 16
s = input(">")
num = "1234567890"
num_count = 0
letters = "qwertyuiopasdfghjklzxcvbnmёйцукенгшщзхъфывапролджэячсмитьбю"
letters = letters + letters.upper()
letters_count = 0
space = " "
space_count = 0
else_count = 0
for i in  s:
    if i in num:
        num_count +=1
    elif i in letters:
        letters_count += 1
    elif i in space:
        space_count += 1
    else:
        else_count += 1
print("количество цифр:" , num_count, "количество букв:" , letters_count, "количество пробелов:" , space_count, "другие символы:" , else_count)

# task 17
s = input(">")
l = s.split()
was =[]
for i in l :
    if i not in was:
        was.append(i)
c = " ".join(was)
print(c)

# task 18
s = input(">")
l = s.split()
a = []
c = ""
for i in l :
    if i[0] == "а" or i[0] == "А":
        a.append(i)
c = " ".join(a)
print(c)

# task 19
s = input(">")
s = s.lower()
ss = ""
for i in s :
    if i in string.punctuation:
        ss += ""
    else:
        ss += i
print(ss)
l = ss.split()
print(l)
n = 0
unig_words = []
out_word = ""
for i in l:
    if i not in unig_words:
        unig_words.append(i)
print(unig_words)
for word in unig_words:
    print(word)
    if l.count(word) > n :
        print(l.count(word))
        n = l.count(word)
        out_word = word
print(out_word)
# task 20
s = input(">")
letters = "qwertyuiopasdfghjklzxcvbnmёйцукенгшщзхъфывапролджэячсмитьбю"
letters_count = 0
up_letters = letters.upper()
up_letters_count = 0
num = string.digits
num_count = 0
space_count = 0
for i in s:
    if i in letters:
        letters_count += 1
    elif i in up_letters:
        up_letters_count += 1
    elif i in num:
        num_count +=1
    elif i == " ":
        space_count += 1
if len(s) >= 8 and letters_count > 1 and up_letters_count > 1 and num_count > 1 and space_count == 0:
    print("пароль подходит ")
else:
    print("пароль не подходит")