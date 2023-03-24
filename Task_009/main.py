# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.
# Пример:
# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random

def checkingInput(message):
    while True:
        n = (input(message))
        if n.isdigit() == False:
            print(f'Не верный тип!')
        else:
            return n
        
def fillingArray(n):
    array = [random.randint(1, n) for _ in range(n)]
    return(array)

def checkingArray(n):
    for i in range (len(array)):
            temp = array[i]
            if temp == n:
                return temp
    
def checkingNumber(array, n):
    print(array)
    for i in range (1, len(array)):
        min = n - i
        max = n + i
        if min == checkingArray(min):
            print(f'Ближайший наименьший элемент > {min}')
            break
        elif max == checkingArray(max):
            print(f'Ближайший наибольший элемент > {max}')
            break
        
n_array = checkingInput(f'Введите размер массива > ')
n_matches = checkingInput(f'Введите число для проверки (от 0 до {n_array}) > ')
if n_matches > n_array or n_matches < 0:
    print(f'Значение числа для проверки вне диапазона!')
else:
    array = fillingArray(int(n_array))
    checkingNumber(array, int(n_matches))