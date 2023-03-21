# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
import random

def checkingInput(message):
    while True:
        n = (input(message))
        if n.isdigit() == False:
            print(f'Не верный тип!')
        else:
            return n

def sumHeadsTails(n):
    heads = 0
    tails = 0
    index = 0
    while index < n:
        index += 1
        coin = random.randint(1, 2)
        if coin == 1:
            heads += 1
        else:
            tails += 1
    if heads < tails:
        print(f'Переворачиваем монеты вверх орлом ({heads}), так как их меньше чем монет вверх решкой ({tails})')
    else:
        print(f'Переворачиваем монеты вверх решкой ({tails}), так как их меньше чем монет вверх орлом ({heads})')

n = checkingInput(f'Введите количество монет > ')
sumHeadsTails(int(n))