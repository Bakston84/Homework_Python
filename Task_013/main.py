# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# Пример:

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def checkingInput(message):
    while True:
        n = (input(message))
        if n.isdigit() == False:
            print(f'Не верный тип!')
        else:
            return n
        
def building_degree(a, b):
    if b == 1:
        return a
    return (a * building_degree(a, b - 1))
    
        
number_a = int(checkingInput('Введите число для возведения в степень > '))
number_b = int(checkingInput('Введите число целой степени > '))
print(f'число {number_a} в степени {number_b}, равно > ', int(building_degree(number_a, number_b)))
