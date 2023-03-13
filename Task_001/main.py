# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

def getSum(n):

    sum = 0
    while (n != 0):

        sum = sum + (n % 10)
        n = n // 10

    return sum

while True:
    n = (input('Введите 3-х значное число >'))
    if n.isdigit() == False:
        print('Не верный тип!')
    else:
        count = 0
        number = int(n)
        while number > 0:
            number //= 10
            count += 1
        if count < 3 or count > 3:
            print('Вы ввели не 3-х значное число!')
        else:
            break

print('Сумма элементов числа, равна:', getSum(int(n)))