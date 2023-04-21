# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input('Введите количество элементов списка: '))
import random
list = []
for i in range(n): 
    list.append(random.randint(0,100))
print(list)
x = int(input("Введите число для сравнения: "))
min = abs(x - list[0])
index = 0
for i in range(1, n):
    count = abs(x - list[i])
    if count < min:
        min = count
        index = i
print(f'{list[index]} наиболее близкое к заданному числу')


