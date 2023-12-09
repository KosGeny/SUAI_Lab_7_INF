import utils.json_service as json_service

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

            elem["name"] = costumer["name"]
            elem["discount_card"] = costumer["discount_card"]

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