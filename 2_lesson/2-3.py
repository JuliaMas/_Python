# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю
# историю наблюдений за погодой. Они обратились к синоптикам,
# а те, в свою очередь, занялись исследованиями статистики
# за прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период,
# в который среднесуточная температура ежедневно
# превышала 0 градусов Цельсия. Напишите программу,
# помогающую синоптикам в работе.

# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50

n = int(input("Введите число: "))

count = 0
result = 0

for i in range(n) :
    temp = int(input(f"{i + 1}-день: "))

    if(temp > 0) :
        count = count + 1

        if(count > result) :
            result = count

    else :
        count = 0

print(f"Количество дней с средней температурой больше 0 градусов: {result}")