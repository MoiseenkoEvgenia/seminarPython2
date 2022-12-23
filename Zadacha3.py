# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ 
# БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для получения 
# случайного int
import random
list = []
for i in range(4):
    list.append(random.randint(0,3))

print(list)
list.sort()

print(list)
list.reverse()

print(list)
