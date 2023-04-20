# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных
import os

# Открываем справочник
def read_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as data:
            data_array = []
            for line in data:
                item = line.replace('\n','').split(sep = ',')
                data_array.append(item)
        return data_array
    else:
        print('Телефонный справочник отсутствует, попробуйте добавить запись!')
        menu()

# Записываем в справочник
def write_file(file_name, data_array):
    with open(file_name, 'w') as data:
        for i in data_array:
            write_element = ','.join(i)
            data.write(f'{write_element}\n')
    menu()

# Добавляем справочник в репозиторий
def add_file(file_name):
    if not os.path.exists(file_name):
        new_item = ['ID', 'last_name', 'first_name', 'second_name', 'phone']
        with open(file_name, 'w+') as data:
            for i in range(len(new_item)):
                write_element = new_item[i]
                data.write(f'{write_element} ')
    else:
        return

# Добавляем запись в справочник
def add_item(file_name, last_name = '', first_name = '', second_name = '', phone = ''):
    add_file(file_name)
    data_array = read_file(file_name) 
    max_id = 0
    for i in range(1,len(data_array)):
        if max_id < int(data_array[i][0]): 
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    last_name = input('\nВведите фамилию: ')
    first_name = input('Введите имя: ')
    second_name = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    new_item = []
    new_item.append(str(next_id))
    new_item.append(last_name)
    new_item.append(first_name)
    new_item.append(second_name)
    new_item.append(phone)
    data_array.append(new_item)
    print('\nКонтакт добавлен!')
    write_file(file_name, data_array)

# Показываем все записи в справочнике
def show_all_items(file_name):
    data_array = read_file(file_name)
    print('\nСписок контактов:')
    for i in range(1,len(data_array)):
        print(f'ID:{data_array[i][0]} Фамилия:{data_array[i][1]} Имя:{data_array[i][2]} Отчество:{data_array[i][3]} Телефон:{data_array[i][4]}')
    menu()

# Ищем пользователя в справочнике
def search_items(file_name, point_menu):
    index = 0
    search = input('\nВведите имя или фамилию для поиска > ')
    data_array = read_file(file_name)
    print('\nРезультаты поиска:')
    for i in range(1,len(data_array)):
        search_element = data_array[i]
        if search_element.count(search):
            print(f'ID:{data_array[i][0]} Фамилия:{data_array[i][1]} Имя:{data_array[i][2]} Отчество:{data_array[i][3]} Телефон:{data_array[i][4]}')
            index += 1
    print(f'Контактов найдено: {index}\n')
    if index > 0 and point_menu == 3:
        edit_item(file_name)
    elif index > 0 and point_menu == 4:
        delete_item(file_name)
    else:
        print('Контакт не найден!')
        menu()

# Удаляем пользователя
def delete_item(file_name):
    delete_id = int (input('Введите ID контакта для удаления его из телефонного справочника > '))
    data_array = read_file(file_name)
    del data_array[delete_id]
    for i in range(1,len(data_array)):
        data_array[i][0] = str(i)
    print(f'\nПользователь с ID {delete_id} - удалён!')
    write_file(file_name, data_array)

# Редактируем пользователя
def edit_item(file_name):
    edit_id = int (input('Введите ID контакта для редактирования > '))
    data_array = read_file(file_name)
    edit_item = data_array[edit_id]
    print(f'ID:{edit_item[0]} Фамилия:{edit_item[1]} Имя:{edit_item[2]} Отчество:{edit_item[3]} Телефон:{edit_item[4]}')
    id = edit_item[0]
    last_name = edit_item[1]
    first_name = edit_item[2]
    second_name = edit_item[3]
    phone = edit_item[4]
    edit_menu(data_array, id, last_name, first_name, second_name, phone)

# Меню редактирования пользователя
def edit_menu(data_array, id, last_name, first_name, second_name, phone):
    print(f'\nМеню редактирования контакта:')
    print(f'1 - Редактировать фамилию')
    print(f'2 - Редактировать имя')
    print(f'3 - Редактировать отчество')
    print(f'4 - Редактировать телефон')
    print(f'5 - Вернуться в меню телефонного справочника\n')
    user_operation = int(input(f'Выберите пункт меню > '))
    if user_operation == 1:
        last_name = input('Введите фамилию: ')
    elif user_operation == 2: 
        first_name = input('Введите имя: ')
    elif user_operation == 3:
        second_name = input('Введите отчество: ')
    elif user_operation == 4:
        phone = input('Введите номер телефона: ')
    elif user_operation == 5:
        menu()
    else:
        edit_menu()
    edit_item = [id, last_name, first_name, second_name, phone]
    data_array[int(id)].clear()
    data_array[int(id)] = edit_item
    print('\nКонтакт изменён!')
    write_file(file_name, data_array)

# Меню справочника
def menu():
    print(f'\nМеню телефонного справочника:')
    print(f'1 - Показать все контакты')
    print(f'2 - Добавить контакт')
    print(f'3 - Изменить контакт')
    print(f'4 - Удалить контакт\n')
    user_operation = int(input(f'Выберите пункт меню > '))
    if user_operation == 1:
        show_all_items(file_name)
    elif user_operation == 2: 
        add_item(file_name)
    elif user_operation == 3:
        search_items(file_name, point_menu = 3)
    elif user_operation == 4:
        search_items(file_name, point_menu = 4)
    else:
        menu()

# Старт программы
file_name = 'Task_19/telephone.txt'
print('\nДобро пожаловать в телефонный справочник!')
menu()