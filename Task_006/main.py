# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

def checkingInput(message):
    while True:
        n = (input(message))
        if n.isdigit() == False:
            print(f'Не верный тип!')
        else:
            return n

def checkingNumbers(first, second):
    checking_first_sum = first // 2
    checking_second_sum = first - checking_first_sum
    multi = checking_first_sum * checking_second_sum
    if multi == second:
        print(f'Задуманные числа: {checking_first_sum} и {checking_second_sum}')
    else:
        print(f'Условия не корректны!')

first = checkingInput(f'Введите сумму чисел > ')
second = checkingInput(f'Введите произведение чисел > ')
checkingNumbers (int(first), int(second))