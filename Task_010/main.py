# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Ввод: ноутбук
# Вывод: 12

def checkingInput(message):
    while True:
        n = (input(message))
        if n.isdigit() == True:
            print(f'Не верный тип!')
        else:
            return n
        
def createDict(dict_sample):
    dict_sample.update(dict.fromkeys(list('AEIOULNSTRАВЕИНОРСТ'), 1))
    dict_sample.update(dict.fromkeys(list('DGДКЛМПУ'), 2))
    dict_sample.update(dict.fromkeys(list('BCMPБГЁЬЯ'), 3))
    dict_sample.update(dict.fromkeys(list('FHVWYЙЫ'), 4))
    dict_sample.update(dict.fromkeys(list('KЖЗХЦЧ'), 5))
    dict_sample.update(dict.fromkeys(list('JXШЭЮ'), 8))
    dict_sample.update(dict.fromkeys(list('QZФЩЪ'), 10))
    return

def checkingKey(list):
    sum = 0
    for i in range(len(list)):
        key = (dict_sample.get(list[i]))
        sum = sum + int(key)
    return sum

dict_sample = dict()
createDict(dict_sample)
list = list(checkingInput(f'Введите слово > ').upper())
print(checkingKey(list))