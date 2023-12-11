import utils.json_service as json_service
import service_base

def id_input_check(partition):
    db = json_service.get_database()
    list_of_id = list(elem["id"] for elem in db[partition])
    # partition = globals().get(partition)
    # list_of_id = partition.get_id()
    flag = True
    while flag:
        try:
            value = int(input('id: '))
            if value in list_of_id:
                flag = False
            else:
                print('Данной записи нет в БД!')
                print('Вы хотите продолжить?' + '\n' + '1 - да' + '\n' + '2 - нет')
                if service_base.IsInt_Range((1,2)) == 2:
                    break
        except:
            print('Ой, что-то пошло нет так! Попробуйте ещё раз!')
    return value

def count_input_check(id, partition, start_count=0):
    db = json_service.get_database()
    while True:
        try:
            print('Количество: ', end='')
            value = int(input())
            if value > 0:
                for i, elem in enumerate(db[partition]):
                    if elem["id"] == id:
                        if elem["count"] + start_count >= value:
                            return value
                        else:
                            print('Превышение количества')
            else:
                print('Количество должно быть больше нуля!')
        except:
            print('Ой, что-то пошло нет так! Попробуйте ещё раз!')

def check_delete(partition_delete, id):
    db = json_service.get_database()
    list_of_id = []
    for elem in db["sellings"]:
        if partition_delete == "cashier_id":
            if elem["cashier_id"] == id:
                list_of_id.append(elem["id"])
        if partition_delete == "costumer_id":
            if elem["costumer_id"] == id:
                list_of_id.append(elem["id"])
        if partition_delete == "medicament_id":
            for elem2 in elem["list_of_medicaments"]:
                if elem2["medicament_id"] == id:
                    list_of_id.append(elem["id"])
    return list_of_id