""""# task 1
n = int(input("введите число>"))
l = list(i ** 2 for i in range(1, n+1))
print(l)
# task 2
n = int(input("введите число>")) # n > 0
l = list(i for i in range(3, n+1, 3 ))
print(l)
# task 3
s = input(">").split()
l = list(len(i) for i in s)
print(l)
# task 4
s = input(">").split()
l = list(int(i) ** 2 for i in s if int(i) < 0)
print(l)
# task 5
s = input(">").split(",")
l = list(i[0] for i in s if i != "")
print(l)
# task 6
s = input(">").split()
l = list("четное"if int(i) % 2 ==0 else "нечетное" for i in s )
print(l)
# task 7
s = input(">").split(",")
l = list(i.strip() for i in s if i.strip() != "")
print(l)
# task 8
n = int(input())
l = list((x,y) for x in range(n) for y in range(x + 1, n + 1))# x + 1 ==> y всегда > x
print(l)
# task 9
s = input(">").split(";")
l =list(j for i in s for j in i.split() if int(j) >0 )
print(l)
# task 10
s = input(">").split()
l = list((int(i)-int(j)) for i in s[0:len(s)-1:2] for j in s[1:len(s)-1:2])
print(l)
# task 11
s = input(">").split()
l = list(filter(lambda i: int(i) > 0, s))
print(l)
# task 12
s = map(int,input(">").split())
l = list(filter(lambda i: i % 3 ==0 or i % 5 == 0 , s))
print(l)
# task 13
s = map(int,input(">").split())
a, b= map(int,input(">").split())
l = list(filter(lambda i: i in range(a,b+1),s))
print(l)
# task 14
s = input(">").split()
l = list(filter(lambda i: i.split(".")[-1] == "py" , s))
print(l)
# task 15
s = input(">").split(",")
l = list(filter(lambda i: int(i.split()[-1]) >= 60, s))
print(l)
# task 16
s = input(">").lower().split(",")
l = list(filter(lambda i: len(i) >=2 and i[0] == i[-1], s))
print(l)
# task 17
s = input(">").split(",")
l = list(filter(lambda i: i.split()[1]== "1" and int(i.split()[0])>= 300 ,s))
print(l)
# task 18
s = list(map(int,input(">").split()))
print(s)
# task 19
s = list(map(str, input(">").strip().title().split(",")))
print(s)
# task 20
s = input(">").split()
l = list(map(lambda i: i[0] + i[-1], s))
print(l)
# task 21
s = input(">").split()
l = list(map(lambda i:str(int(i)//60) + " ; " + str(int(i)%60), s))
print(l)
# task 22 что?
s = input(">").split()
l = list(map(lambda i:str(int(i)*100), s))
print(l)
# task 23
s = list(map(str,input(">").split(",")))
l = list(int(i.split()[0])*int(i.split()[-1]) for i in s)
print(l)
# task 24
a = input(">").split()
b = input(">").split()
l = list(map(lambda i, j: int(i) - int(j) , a,b))
print(l)
# task 25
s = input(">").split()
l = list(int(i)**2 for i in s if int(i) %2!=0)
print(l)
# task 26
s = input(">").split(",")
l = list(map(str,(filter(lambda i:int(i.split()[-1])>=18 , s))))
out = list(i.split()[0] for i in l)
print(out)
# task 27
s = map(int,input().split())
l = list(filter(lambda i: abs(i)>5, s))# abs() - модуль
out = list(map(abs,l))
print(out)
# task 28
s = input(">").lower().split(",")
print(s)
l = list(filter(lambda i: i.strip().startswith("го"), s))
print(l)
# task 29
s = list(map(int,input(">").split()))
l = list(int(i)**2 for i in s if int(i) %2!=0)
print(l)
l1 = list(i**2 for i in s)
 # делать проверку на знак не имеет необходимостм, т.к. любое число вквадрате является положительным
print(l1)
# в итоге в 1 списки мы имеем только квадрыты чисел с заданным условием, когда во втором расположились квадраты всех чисел из списка
# task 30
s = list(map(int,input(">").split()))
l = filter(bool, s)
print("1", list(l))
print("2", list(l))
a = map(abs, s)
print("1", list(a))
print("2", list(a))

"""