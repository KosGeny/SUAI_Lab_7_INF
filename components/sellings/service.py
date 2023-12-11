import utils.json_service as json_service
import utils.checker as checker
from components.medicaments.selling_refund import selling, refund
import service_base

def generation_dictionary(candidate={"cashier_id": None, "costumer_id": None, "list_of_medicaments": [], "income": None}, keys=["cashier_id", "costumer_id", "list_of_medicaments"]):
    for key in keys:
        if key == "cashier_id":
            print('Введите id сотрудника')
            candidate[key] = checker.id_input_check("cashiers")
        if key == "costumer_id":
            print('Введите id покупателя')
            candidate[key] = checker.id_input_check("cashiers")
        if key == "list_of_medicaments":
            flag = True
            if len(candidate["list_of_medicaments"]) == 0 and flag:
                flag = False
                print('Заполните список лекарств')
                while True:
                    print('Введите id лекарства')
                    medicament_id = checker.id_input_check("medicaments")
                    print('Введите количество')
                    count = checker.count_input_check(medicament_id, "medicaments")
                    if count != 0:
                        medicament_count, price = selling(medicament_id, count)
                        candidate["list_of_medicaments"].append({"medicament_id": medicament_id, "count": count, "price": price})
                    else:
                        print('Данного лекарства нет на складе')
                    #income += price
                    print('Продолжить ввод следующего лекарства?     1 - да, 2 - нет')
                    if service_base.IsInt_Range((1,2)) == 2:
                        break
                income = 0
                for elem in candidate["list_of_medicaments"]:
                    income += elem["price"]
                candidate["income"] = income

            if len(candidate["list_of_medicaments"]) != 0 and flag:
                flag = False
                print('Выберите действие, которое нужно совершить со списком проданных лекарств' + '\n' + '1 - Изменить количество одного лекарства' + '\n' + '2 - Удалить из списка лекарство' + '\n' + '3 - Добавить лекарства')

                action = service_base.IsInt_Range((1,2,3))
                if action == 1: #обновление записи
                    list_of_id = [elem["medicament_id"] for elem in candidate["list_of_medicaments"]]
                    print('Введите id лекарства')
                    medicament_id = service_base.IsInt_Range(list_of_id)
                    for i, elem in enumerate(candidate["list_of_medicaments"]):
                        if elem["medicament_id"] == medicament_id:
                            count = checker.count_input_check(medicament_id, "medicaments", elem["count"])
                            if count != 0:
                                refund(medicament_id, elem["count"])
                                candidate["list_of_medicaments"][i]["count"], candidate["list_of_medicaments"][i]["price"] = selling(medicament_id, count)
                            else:
                                print('Данного лекарства не достаточно, или его нет на складе!')

                            if candidate["list_of_medicaments"][i]["count"] == 0:
                                candidate["list_of_medicaments"].pop(i)
                    income = 0
                    for elem in candidate["list_of_medicaments"]:
                        income += elem["price"]
                    candidate["income"] = income

                elif action == 2: #удаление записи
                    list_of_id = [elem["medicament_id"] for elem in candidate["list_of_medicaments"]]
                    print('Введите id лекарства')
                    medicament_id = service_base.IsInt_Range(list_of_id)
                    for i, elem in enumerate(candidate["list_of_medicaments"]):
                        if elem["medicament_id"] == medicament_id:
                            refund(medicament_id, elem["count"])
                            candidate["list_of_medicaments"].pop(i)
                    income = 0
                    for elem in candidate["list_of_medicaments"]:
                        income += elem["price"]
                    candidate["income"] = income

                elif action == 3: #добавление записей ПРОВЕРИТЬ ЕСТЬ ЛИ ДАННЫЙ ID
                    print('Заполните список лекарств, которые хотите добавить')
                    while True:
                        print('Введите id лекарства')
                        medicament_id = checker.id_input_check("medicaments")
                        for i, elem in enumerate(candidate["list_of_medicaments"]):
                            if elem["medicament_id"] == medicament_id:
                                print('Такое лекарство уже есть в списке. При добавлении будет обновлено количество проданного лекарства в уже существующей записи.')
                                print('Введите количество')
                                count = checker.count_input_check(medicament_id, "medicaments")
                                if count != 0:
                                    candidate["list_of_medicaments"][i]["count"], candidate["list_of_medicaments"][i]["price"] = selling(medicament_id, count)
                                    candidate["list_of_medicaments"][i]["count"] += elem["count"]
                                    candidate["list_of_medicaments"][i]["price"] += elem["price"]
                                else:
                                    print('Данного лекарства не достаточно, или его нет на складе!')
                                break
                        else:
                            print('Введите количество')
                            count = checker.count_input_check(medicament_id, "medicaments")
                            if count != 0:
                                medicament_count, price = selling(medicament_id, count)
                                candidate["list_of_medicaments"].append({"medicament_id": medicament_id, "count": count, "price": price})
                            else:
                                print('Данного лекарства не достаточно, или его нет на складе!')
                        print('Продолжить ввод следующего лекарства?     1 - да, 2 - нет')
                        if service_base.IsInt_Range((1, 2)) == 2:
                            break
                    income = 0
                    for elem in candidate["list_of_medicaments"]:
                        income += elem["price"]
                    candidate["income"] = income

    return candidate

def get_id():
    db = json_service.get_database()
    return list(elem["id"] for elem in db["sellings"])

def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["sellings"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["sellings"]


def update_one_by_id(id, selling):
    db = json_service.get_database()

    for i, elem in enumerate(db["sellings"]):
        if elem["id"] == id:
            db["sellings"][i] = {"id": id, **selling}
            json_service.set_database(db)
            return 'Успешно!'

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["sellings"]):
        if elem["id"] == id:

            for elem2 in elem["list_of_medicaments"]:
                refund(elem2["medicament_id"], elem2["count"])

            db_refund = json_service.get_database()
            candidate = db_refund["sellings"].pop(i)
            json_service.set_database(db_refund)

            return 'Успешно!'

    return {"message": f"Элемент с {id} не найден"}


def create_one(selling):
    db = json_service.get_database()

    last_selling_id = get_all()[-1]["id"]
    db["sellings"].append({"id": last_selling_id + 1, **selling})

    json_service.set_database(db)

    return 'Успешно!'