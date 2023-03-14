# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

def checkingInput(message):
    while True:
        n = (input(message))
        if n.isdigit() == False:
            print('Не верный тип!')
        else:
            return n

def dividingNumber(n, m, k):
    sum = (n * m)
    if k < sum and (k % m == 0 or k % n == 0):
        print('Шоколадку можно разломить на два прямоугольника')
    else:
        print('Увы, шоколадка остаётся моей!')
    return

n = checkingInput('Введите количество долек шоколада (n) > ')
m = checkingInput('Введите количество долек шоколада (m) > ')
k = checkingInput('Сколько долек отломить? > ')
dividingNumber(int(n), int(m), int(k))