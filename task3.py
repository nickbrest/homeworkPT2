# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input('Введите число: '))
array = []
sum = 0 
for i in range(1, n + 1):
    temp = int(round((1 + 1 / i) ** i, 0))
    array.append(temp)
    sum += temp
print(array, sum)