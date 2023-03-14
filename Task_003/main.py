# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

def checkingInput():
    while True:
        index = 6
        n = (input('Введите 6-ти значное число > '))
        if n.isdigit() == False:
            print('Не верный тип!')
        else:
            count = 0
            number = int(n)
            while number > 0:
                number //= 10
                count += 1
            if count != index:
                print('Вы ввели не 6-ти значное число!')
            else:
                searchCombination(n)
                break

def searchCombination(n):
    array = [int(i) for i in str(n)]
    first = 0
    second = 0
    for i in range(0, 3):
        first += array[i]
    for i in range(3, 6):
        second += array[i]
    if first == second:
        print('Билет с номером', n, 'счастливый!')
        return
    else:
        print('Билет с номером', n, 'не счастливый!')
        return

checkingInput()