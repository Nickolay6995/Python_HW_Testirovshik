# 4.1[22]: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Если таких чисел нет - выдать внятное диагностическое сообщение
# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры

# Примеры/Тесты:
# Input1: 2 4 6 8 10 12 10 8 6 4 2
# Input2: 3 6 9 12 15 18
# Output: 6 12     Обратите внимание: Без скобочек, в одну строку

# Input1: 2 4 6 8 10 10 8 6 4 2
# Input2: 3 9 12 15 18
# Output: Повторяющихся чисел нет

n1 = {2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2}
n2 = {3, 12, 6, 9, 15, 18}


n3 = (n1.intersection(n2))

s_list = sorted(n3)

if len(s_list) == 0:
    print("Повторяющихся чисел нет")
else:
    for i in s_list:
        print(i, end=" ")