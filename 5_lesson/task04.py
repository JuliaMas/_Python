# Дано натуральное число N и последовательность
# из N элементов. Требуется вывести эту
# последовательность в обратном порядке.

# Примечание. В программе запрещается
# объявлять массивы и использовать
# циклы (даже для ввода и вывода).


n = int(input("Введите n: "))
def num_s(n):
    if n == 0:
        return ''
    res = input()
    return num_s(n - 1) + f'{res} '

print(num_s(n))