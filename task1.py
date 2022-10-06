# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = float(input('Введите число: '))
summ = 0
temp = len(str(number))
number *= 10 ** temp
print(number)
while number > 0:
    summ += number % 10
    number //= 10

print(f'Сумма цифр числа равна: {int(summ)}')
