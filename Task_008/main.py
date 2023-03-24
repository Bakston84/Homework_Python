# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
# Пример:
# Ввод: 5
# Ввод: 1
# 1 2 1 2 2
# Вывод: 2

import random

def checkingInput(message):
    while True:
        n = (input(message))
        if n.isdigit() == False:
            print(f'Не верный тип!')
        else:
            return n

def fillingArray(n):
    array = [random.randint(1, n // 2) for _ in range(n)]
    return(array)
     
n_array = checkingInput(f'Введите размер массива > ')
n_matches = checkingInput(f'Введите число для поиска совпадений > ')
array = fillingArray(int(n_array))
print(array.count(int(n_matches)))
