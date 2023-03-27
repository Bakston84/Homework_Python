# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

def checkingInput(message):
    while True:
        n = (input(message))
        if n.isdigit() == False:
            print(f'Не верный тип!')
        else:
            return n
        
def inputElements(size_elements, num):
    elements = set()
    for i in range (int(size_elements)):
        elements.add(int(checkingInput(f'Введите {i + 1} элемент {num}-го множества > ')))
    return elements

n = checkingInput(f'Введите количество элементов 1-го множества > ')
n_elements = inputElements(n, 1)
m = checkingInput(f'Введите количество элементов 2-го множества > ')
m_elements = inputElements(m, 2)
for i in n_elements | m_elements:
    print(i, end=' ')