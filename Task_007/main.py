# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

def checkingInput(message):
    while True:
        n = (input(message))
        if n.isdigit() == False:
            print(f'Не верный тип!')
        else:
            return n

def integerPowersTwo(n):
    i = 1
    while i <= n:
        print(i, end = f' ')
        i = i * 2
   
n = checkingInput(f'Введите число > ')
integerPowersTwo(int(n))