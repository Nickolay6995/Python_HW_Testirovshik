# 1.2[4]. Петя, Катя и Сережа делают из бумаги журавликов. 
#Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
#что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Примеры/Тесты:
# 6 >>>  1  4  1
# 24 >>> 4  16  4
# 60 >>> 10  40  10

def Get_and_chek_number():
    flag = True
    num = int(input("Введите число: \n"))
    while flag:
        if num<0: 
            print("Неправильное число")
            num = int(input("Введите число: \n"))
        else:
            flag = False
            print("Правильное число")
    return num

def Number_of_cranes(num):
    x = num//6
    Katy = num - x*2
    print(f'У Кати {Katy} журавликов')
    print(f'У Пети и Серёжи по {x} журавликов')

S = Get_and_chek_number()
Number_of_cranes(S)