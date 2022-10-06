# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.

import random

r = list(range(10))
print(r)
for i in r:
    a = random.randint(0, len(r) - 1)
    temp = r[i]
    r[i] = r[a]
    r[a] = temp
print(r)
