# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.
# x + y = S, 
# x*y = P          Sx - x^2 = P  ну или x^2 - Sx + P = 0

s = int(input("Введите сумму загаданных чисел "))              
p = int(input("Введите произведение загаданных чисел "))
a = 1
b = int(-s)
c = int(p)
import math
discr = float(b*b - 4*a*c)
if discr < 0.000001:
    x = int (-b / 2*a)
else:
    x = int ((-b + math.sqrt(discr)) / (2 * a))
y = int (s - x)
print(x, y)


