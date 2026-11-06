# task 6
warehouse_1 = {"ручка": 10, "тетрадь": 5}
warehouse_2 = {"ручка": 7, "карандаш": 12}
whole = warehouse_1.copy()
for i in warehouse_2:
    if i not in whole:
        whole[i] = warehouse_2[i]
    else:
        whole[i] += warehouse_2[i]
print(whole)