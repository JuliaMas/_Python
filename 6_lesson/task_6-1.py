# Даны два массива чисел. Требуется вывести те
# элементы первого массива (в том порядке,
# в каком они идут в первом массиве),
# которых нет во втором массиве.

# Пользователь вводит число N - количество
# элементов в первом массиве,
# затем N чисел - элементы массива.
# Затем число M - количество элементов
# во втором массиве. Затем элементы второго массива

# 7
# 3 1 3 4 2 4 12

# 6
# 4 15 43 1 15 1


# list1 = [input(f"{i+1}: ") for i in range(int(input("enter the size of first arrray: ")))]
# list2= [input(f"{i+1}: ") for i in range(int(input("enter the size of first arrray: ")))]
# list3= [i for i in list1  if i not in list2]

# print(list1)
# print(list2)
# print(list3)

# можно списки сразу вот так делать: list1 = [input() for i in range(int(input('Введите размер первого массива: ')))]

n = int(input("enter the size of first array "))
m = int(input("enter the size of second array "))
list_1 = [input() for i in range(n)]
list_2 = [input() for i in range(m)]
list = [i for i in list_1 if i not in list_2]
print(list_1)
print(list_2)

print(list)