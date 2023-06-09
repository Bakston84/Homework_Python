# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

def checkingInput():
    while True:
        n = (input('Введите количество журавликов > '))
        if n.isdigit() == False:
            print('Не верный тип!')
        else:
            distributeNumber(n)
            break

def distributeNumber(n):
    number = int(n)
    k = (number / 3) * 2
    s = (number / 3) / 2
    if s % 2 != 0:
        print('Решение не возможно, количество журавликов у Пети и Серёжи не равно целому числу!')
        checkingInput()
    else:
        print('Катя сделала', int(k), 'журавликов, а Петя и Серёжа по', int(s))

checkingInput()