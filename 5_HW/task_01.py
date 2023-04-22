#  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# a = int(input("Введите число А: "))
# b = int(input("Введите число В: "))
# def degree (a, b):
#     if a == 0:
#         return 0
#     elif b > 1:
#         return a * degree(a, b-1)
#     elif b == 0:
#         return 1
#     else:
#         return a
# print(degree(a, b))


a = float(input("Введите число А: "))
b = float(input("Введите число В: "))
def degree (a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        return 1 / (a * degree(a, -b - 1))
    else:
       return a * degree(a, b - 1) 
   
print(degree(a, b))


