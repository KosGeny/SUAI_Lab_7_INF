import utils.json_service as json_service
import service_base

def generation_dictionary(candidate={"name": None, "age": None, "contacts": {"email": None, "phone": None}}, keys=["name", "age", "contacts"]):
    for key in keys:
        if key == "name":
            print('Введите ФИО сотрудника')
            candidate[key] = input()
        if key == "age":
            print('Введите возраст сотрудника')
            candidate[key] = service_base.IsInt_length(2)
        if key == "contacts":
            if candidate[key]["email"] != None:
                print('Вы уверены, что хотите изменить адрес электронной почты?' + '\n' + '1 - да' + '\n' + '2 - нет')
                if service_base.IsInt_Range((1, 2)) == 1:
                    print('Введите адрес электронной почты')
                    candidate[key]["email"] = input()
            else:
                print('Введите адрес электронной почты')
                candidate[key]["email"] = input()
            if candidate[key]["phone"] != None:
                print('Вы уверены, что хотите изменить номер телефона?' + '\n' + '1 - да' + '\n' + '2 - нет')
                if service_base.IsInt_Range((1, 2)) == 1:
                    print('Введите номер телефона. Вводить +7 не нужно!')
                    candidate[key]["phone"] = '+7' + str(service_base.IsInt_length(10))
            else:
                print('Введите номер телефона. Вводить +7 не нужно!')
                candidate[key]["phone"] = '+7' + str(service_base.IsInt_length(10))
    return candidate

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
            db["cashiers"][i] = {"id": id, **cashier}
            json_service.set_database(db)
            return 'Успешно!'

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["cashiers"]):
        if elem["id"] == id:

            candidate = db["cashiers"].pop(i)
            json_service.set_database(db)

            return 'Успешно!'

    return {"message": f"Элемент с {id} не найден"}


def create_one(cashier):
    db = json_service.get_database()

    last_cashier_id = get_all()[-1]["id"]
    db["cashiers"].append({"id": last_cashier_id + 1, **cashier})

    json_service.set_database(db)

    return 'Успешно!'