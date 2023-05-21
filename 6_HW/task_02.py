# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
#диапазон задаем сами

n = int(input('Введите количество элементов массива: '))
import random
list_1 =[]
for i in range(n): 
    list_1.append(random.randint(-10,50))
print(list_1)
list_2 = []
min = int(input('min: '))      #границы диапазона
max = int(input('max: '))
for i in range(len(list_1)):
     if min <= list_1[i] <= max:
         print(i, end=' ')


# nums_list = [int(i) for i in input().split()]
# num_min = int(input())
# num_max = int(input())

# print([ind for ind, val in enumerate(nums_list) if num_min <= val <= num_max])