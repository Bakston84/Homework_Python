# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# Пример:

# 2 2
# 4

def checkingInput(message):
    while True:
        n = (input(message))
        if n.isdigit() == False:
            print(f'Не верный тип!')
        else:
            return n
        
def sum_numbers(a, b):
    if b == 0:
        return a
    return (sum_numbers(a + 1, b - 1))



        
number_a = int(checkingInput('Введите первое число > '))
number_b = int(checkingInput('Введите второе число > '))
print(f'Сумма чисел {number_a} и {number_b}, равна > ', int(sum_numbers(number_a, number_b)))