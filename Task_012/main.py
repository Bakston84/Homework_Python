# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
# различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать 
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

def checkingInput(message):
    while True:
        n = (input(message))
        if n.isdigit() == False:
            print(f'Не верный тип!')
        else:
            return n
        
def inputElements(n):
    elements = list()
    for i in range (int(n)):
        elements.append(int(checkingInput(f'Введите количество ягод на {i + 1} кусте > ')))
    return elements

def maxElement(array):
    array_count = list()
    for i in range(len(array)):
        if i == 0:
            array_count.append(array[i] + array[i + 1] + array[len(array) - 1])
        elif i == len(array) - 1:
            array_count.append(array[i - 1] + array[i] + array[0])
        else: 
            array_count.append(array[i - 1] + array[i] + array[i + 1])
    max_element = max(array_count)
    index_max_element = array_count.index(max(array_count))
    print(f'Сбор максимального количества ягод ({max_element}) будет с {index_max_element + 1}-го куста')
        
n = int(checkingInput(f'Введите количество кустов на грядке > '))
array = inputElements(n)
max_array_count = maxElement(array)