import utils.json_service as json_service
import service_base

def generation_dictionary(keys = ["name", "age", "contacts"]):
    cashier = {}
    for key in keys:
        if key == "name":
            print('Введите ФИО сотрудника')
            cashier[key] = input()
        if key == "age":
            print('Введите возраст сотрудника')
            cashier[key] = service_base.IsInt_length(2)
        if key == "contacts":
            print('Введите адрес электронной почты')
            cashier[key]["email"] = input()
            print('Введите номер телефона')
            print('+7', end='')
            cashier[key]["phone"] = service_base.IsInt_length(10)
    return cashier

def get_id():
    db = json_service.get_database()
    return list(elem["id"] for elem in db["cashiers"])

def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["cashiers"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["cashiers"]


def update_one_by_id(id, cashier):
    db = json_service.get_database()

    for i, elem in enumerate(db["cashiers"]):
        if elem["id"] == id:

            elem["name"] = cashier["name"]
            elem["contacts"] = cashier["contacts"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["cashiers"]):
        if elem["id"] == id:

            candidate = db["cashiers"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(cashier):
    db = json_service.get_database()

    last_cashier_id = get_all()[-1]["id"]
    db["cashiers"].append({"id": last_cashier_id + 1, **cashier})

    json_service.set_database(db)