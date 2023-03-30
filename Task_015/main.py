# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def checkingInput(message):
    while True:
        n = (input(message))
        if n.isdigit() == False:
            print(f'Не верный тип!')
        else:
            return n
        
def arithmeticProgression(a1, d, k):
    result = []
    for i in range(k):
        result.append(a1 + i * d)
    return result

        
a1 = int(checkingInput('Введите первый элемент члена a1 => '))
d = int(checkingInput('Введите разность Арифметической Прогрессии => '))
k = int(checkingInput('Введите последний элемент члена k => '))

print(arithmeticProgression(a1, d, k))