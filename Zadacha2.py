# Задайте список из n чисел последовательности (1 + 1/n)**n, 
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

n = int(input("Введите значение n: "))
total = 0
print('[', end='')
for i in range(1, n+1):
    res = round((1 + 1/i)**i, 2)
    print(res, end=', ')
    total += res
print(']')
print(f'Сумма: {total}')
