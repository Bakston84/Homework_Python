# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

def checkingInput(message):
    while True:
        n = (input(message))
        if n.isdigit() == False:
            print(f'Не верный тип!')
        else:
            return n
        
def fillingArray():
    array = [random.randint(1, 10) for _ in range(10)]
    return(array)

def searchIndexRange(list, min_n, max_n):
    list_index = []
    for i in range (len(list)):
        if list[i] >= min_n and list[i] <= max_n:
            list_index.append(i)
    return(list_index)

list = (fillingArray())
print(f'Массив => {list}')
arr_min = int(checkingInput('Введите минимальный диапазон элементов массива > '))
arr_max = int(checkingInput('Введите максимальный диапазон элементов массива > '))
print(f'Индексы заданного диапазона элементов в массиве > {searchIndexRange(list, arr_min, arr_max)}')