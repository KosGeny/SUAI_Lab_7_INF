import components.medicaments.service as medicaments
import components.cashiers.service as cashiers
import components.costumers.service as costumers
import components.sellings.service as sellings

def id_input_check(list_of_id):
    flag = True
    while flag:
        try:
            value = int(input('Введите id нужной записи: '))
            if value in list_of_id:
                flag = False
                print('Запись найдена!')
            else:
                print('Данной записи нет в БД!')
        except:
            print('Ой, что-то пошло нет так! Попробуйте ещё раз!')
    return value

def pattern():
    dict_medicaments = {"id" : None, "name" : None, "company" : None, "recipe_is_required" : None, "count": None, "price" : None}
    for key in dict_medicaments.keys():
        if key in ("id", "count", "price"):
            dict_medicaments[key] = input(f'{key}')
        else:
            dict_medicaments[key] = input(f'{key}')

def crud(partition, operation):
    if operation == 1:
        dict_medicaments = {"id": None, "name": None, "company": None, "recipe_is_required": None, "count": None,
                         "price": None}
        for key in dict_medicaments.keys():
            if key in ("id", "count", "price"):
                print('!')
                dict_medicaments[key] = input(f'{key}')
            else:
                dict_medicaments[key] = input(f'{key}')
        return partition.create_one(dict_medicaments)
    if operation == 2:
        id = id_input_check(partition.get_id())
        return partition.get_one_by_id(id)
    if operation == 3:
        id = id_input_check(partition.get_id())
        return
    if operation == 4:
        id = id_input_check(partition.get_id())
        return partition.delete_one_by_id(id)

print('Добро пожаловать в БД аптеки "Ригла"')

print('Выберите раздел БД' + '\n' + '1 - Лекарства' + '\n' + '2 - Кассиры' + '\n' + '3 - Покупатели' + '\n' + '4 - Продажи')
flag = True
while flag:
    try:
        partition = int(input())
        if partition in (1, 2, 3, 4):
            flag = False
            print('Win')
        else:
            print('again')
    except:
        print('ijrjgirg')

print('Какую операцию вы хотите совершить?'+ '\n' + '1 - Создать новую запись' + '\n' + '2 - Получить все записи' + '\n' + '3 - Получить одну запись' + '\n' + '4 - Обновить данные' + '\n' + '5 - Удалить запись')

flag = True
while flag:
    try:
        operation = int(input())
        if operation in (1, 2, 3, 4, 5):
            flag = False
            print('Win')
        else:
            print('again')
    except:
        print('ijrjgirg')

partition = medicaments
print(crud(partition, operation))