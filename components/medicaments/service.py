import utils.json_service as json_service
import service_base


def generation_dictionary(keys = ["name", "company", "count", "price"]):
    medicament = {}
    for key in keys:
        if key == "name":
            print('Введите название препарата')
            medicament[key] = input()
        if key == "company":
            print('Введите название производителя')
            medicament[key] = input()
        if key == "count":
            print('Введите количество товара')
            medicament[key] = service_base.IsInt()
        if key == "price":
            print('Введите цену за единицу товара')
            medicament[key] = service_base.IsInt()
    return medicament

def get_id():
    db = json_service.get_database()
    return list(elem["id"] for elem in db["medicaments"])

def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["medicaments"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()
    return db["medicaments"]


def update_one_by_id(id, medicament):
    db = json_service.get_database()

    for i, elem in enumerate(db["medicaments"]):
        if elem["id"] == id:

            elem["name"] = medicament["name"]
            elem["company"] = medicament["company"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["medicaments"]):
        if elem["id"] == id:

            candidate = db["medicaments"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(medicament):
    db = json_service.get_database()

    last_medicament_id = get_all()[-1]["id"]
    db["medicaments"].append({"id": last_medicament_id + 1, **medicament})

    json_service.set_database(db)