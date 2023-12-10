import components.medicaments.service as medicaments
import components.cashiers.service as cashiers
import components.costumers.service as costumers
import components.sellings.service as sellings
import utils.checker as checkID
import service_base



def crud(partition, operation):
    if operation == 1:
        partition = globals().get(partition)
        return partition.create_one(partition.generation_dictionary())

    if operation == 2:
        partition = globals().get(partition)
        return partition.get_all()

    if operation == 3:
        id = checkID.id_input_check(partition)
        partition = globals().get(partition)
        return partition.get_one_by_id(id)

    if operation == 4:
        id = checkID.id_input_check(partition)
        partition = globals().get(partition)
        print('Используйте цифры 1 и 2, чтобы выбрать, что вы хотите изменить. 1 - да   2 - нет')
        list_of_keys = []
        for i, key in enumerate(partition.get_one_by_id(id).keys()):
            if key != "id":
                print(f'{i} - {key}')
                if service_base.IsInt_Range((1, 2)) == 1:
                    list_of_keys.append(key)
        return partition.update_one_by_id(id, partition.generation_dictionary(partition.get_one_by_id(id), keys=list_of_keys))

    if operation == 5:
        id = checkID.id_input_check(partition)
        partition_delete = str(partition)[:-1] + "_id"
        partition = globals().get(partition)
        if partition != sellings:
            if sellings.check_delete(partition_delete, id):
                return partition.delete_one_by_id(id)
            else:
                return 'Операция не может быть совершена, т. к. может быть нарушена целостность БД'
        else:
            partition.delete_one_by_id(id)


print('Добро пожаловать в БД аптеки "Ригла"')

partitions = ["medicaments", "cashiers", "costumers", "sellings"]
print('Выберите раздел БД')
for i, elem in enumerate(partitions):
    print(f'{i+1} - {elem}')
partition = partitions[service_base.IsInt_Range((1, 2, 3, 4))-1]

print('Какую операцию вы хотите совершить?'+ '\n' + '1 - Создать новую запись' + '\n' + '2 - Получить все записи' + '\n' + '3 - Получить одну запись' + '\n' + '4 - Обновить данные' + '\n' + '5 - Удалить запись')
operation = service_base.IsInt_Range((1, 2, 3, 4, 5))

try:
    print(crud(partition, operation))
except:
    print('Чтобы взаимодействовать с базой данных запустите программу снова')