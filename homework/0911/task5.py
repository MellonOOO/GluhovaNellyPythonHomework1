#task 5
a = list(map(str, input(">").split()))
count = {}
for i in set(a):
    count[i] = a.count(i)
print(count)

