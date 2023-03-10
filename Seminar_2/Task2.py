# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# Примеры/Тесты:
# 4 4 -> 2 2
# 5 6 -> 2 3

X = int(input())
Y = int(input())

X_1 = (X - int((X ** 2 - 4 * Y) ** 0.5)) // 2
Y_1 = (X + int((X ** 2 - 4 * Y) ** 0.5)) // 2

print(f'{X} {Y} -> {X_1} {Y_1}')