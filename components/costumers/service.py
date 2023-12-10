import utils.json_service as json_service
import service_base

def generation_dictionary(costumer={"name": None, "discount_card": None, "contacts": {"email": None, "phone": None}}, keys=["name", "discount_card", "contacts"]):
    for key in keys:
        if key == "name":
            print('Введите ФИО покупателя')
            costumer[key] = input()
        if key == "discount_card":
            print('Введите номер карты постоянного покупателя')
            costumer[key] = service_base.IsInt_length(10)
        if key == "contacts":
            if costumer[key]["email"] != None:
                print('Вы уверены, что хотите изменить адрес электронной почты?' + '\n' + '1 - да' + '\n' + '2 - нет')
                if service_base.IsInt_Range((1, 2)) == 1:
                    print('Введите адрес электронной почты')
                    costumer[key]["email"] = input()
            else:
                print('Введите адрес электронной почты')
                costumer[key]["email"] = input()
            if costumer[key]["phone"] != None:
                print('Вы уверены, что хотите изменить номер телефона?' + '\n' + '1 - да' + '\n' + '2 - нет')
                if service_base.IsInt_Range((1, 2)) == 1:
                    print('Введите номер телефона. Вводить +7 не нужно!')
                    costumer[key]["phone"] = '+7' + str(service_base.IsInt_length(10))
            else:
                print('Введите номер телефона. Вводить +7 не нужно!')
                costumer[key]["phone"] = '+7' + str(service_base.IsInt_length(10))
    return costumer

def get_id():
    db = json_service.get_database()
    return list(elem["id"] for elem in db["costumers"])

def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["costumers"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["costumers"]


def update_one_by_id(id, costumer):
    db = json_service.get_database()

    for i, elem in enumerate(db["costumers"]):
        if elem["id"] == id:
            db["costumers"][i] = {"id": id, **costumer}
            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["costumers"]):
        if elem["id"] == id:

            candidate = db["costumers"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(costumer):
    db = json_service.get_database()

    last_costumer_id = get_all()[-1]["id"]
    db["costumers"].append({"id": last_costumer_id + 1, **costumer})

    json_service.set_database(db)