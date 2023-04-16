# Напишите программу, которая принимает
# на вход строку, и отслеживает, сколько
# раз каждый символ уже встречался.
# Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# a a a b c a a d c d d

string = "a a a b c a a d c d d".split()

new_dict = {}.fromkeys(string, 0)

for i in string:
    print(f"{i}_{new_dict[i]}" if new_dict[i] else i, end=" ")
    new_dict[i] += 1