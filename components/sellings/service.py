import utils.json_service as json_service

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