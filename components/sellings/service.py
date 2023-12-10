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
            if len(candidate["list_of_medicaments"]) != 0:
                print('Выберите действие, которое нужно совершить со списком проданных лекарств' + '\n' + '1 - Изменить количество одного лекарства' + '\n' + '2 - Удалить из списка лекарство' + '\n' + '3 - Добавить лекарства')

                if service_base.IsInt_Range((1,2,3)) == 1:
                    list_of_id = [elem["medicament_id"] for elem in candidate["list_of_medicaments"]]
                    print('Введите id лекарства:')
                    medicament_id = service_base.IsInt_Range(list_of_id)
                    for i, elem in enumerate(candidate["list_of_medicaments"]):
                        if elem["medicament_id"] == medicament_id:
                            count = checker.count_input_check(medicament_id, "medicaments", start_count=elem["count"])
                            refund(medicament_id, elem["count"])
                            candidate["list_of_medicaments"][i]["count"] = count
                    income = 0
                    for elem in candidate["list_of_medicaments"]:
                        income += elem["price"]
                    candidate["income"] = income

                if service_base.IsInt_Range((1,2,3)) == 3:
                    while True:
                        print(f'Введите id лекарства: ', end='')
                        medicament_id = checker.id_input_check("medicaments")
                        print(f'Введите количество: ', end='')
                        medicament_count = checker.count_input_check(medicament_id, "medicaments")
                        candidate["list_of_medicaments"].append(
                            {"medicament_id": medicament_id, "count": medicament_count})
                        print('Продолжить ввод?     1 - да, 2 - нет')
                        if service_base.IsInt_Range((1, 2)) == 2:
                            break
            if len(candidate["list_of_medicaments"]) == 0:
                income = 0
                while True:
                    print(f'Введите id лекарства: ', end='')
                    medicament_id = checker.id_input_check("medicaments")
                    print(f'Введите количество: ', end='')
                    medicament_count, price = selling(medicament_id)
                    candidate["list_of_medicaments"].append({"medicament_id": medicament_id, "count": medicament_count, "price": price})
                    income += price
                    print('Продолжить ввод?     1 - да, 2 - нет')
                    if service_base.IsInt_Range((1,2)) == 2:
                        break
                candidate["income"] = income
    return candidate

def check_delete(partition_delete, id):
    db = json_service.get_database()
    for elem in db["sellings"]:
        if partition_delete == "cashier_id":
            if elem["cashier_id"] == id:
                return False
        if partition_delete == "costumer_id":
            if elem["costumer_id"] == id:
                return False
        if partition_delete == "medicament_id":
            for elem2 in elem["list_of_medicaments"]:
                if elem2["medicament_id"] == id:
                    return False
    return True
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

    return db["medicaments"]


def update_one_by_id(id, selling):
    db = json_service.get_database()

    for i, elem in enumerate(db["sellings"]):
        if elem["id"] == id:
            db["sellings"][i] = {"id": id, **selling}
            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["sellings"]):
        if elem["id"] == id:

            candidate = db["sellings"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(selling):
    db = json_service.get_database()

    last_selling_id = get_all()[-1]["id"]
    db["sellings"].append({"id": last_selling_id + 1, **selling})

    json_service.set_database(db)