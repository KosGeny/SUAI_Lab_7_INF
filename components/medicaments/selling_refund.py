import utils.json_service as json_service

def selling(id, value):
    db = json_service.get_database()

    for i, elem in enumerate(db["medicaments"]):
        if elem["id"] == id:
            db["medicaments"][i]["count"] -= value
            income = elem["price"] * value
            json_service.set_database(db)
            return value, income

def refund(id, count):
    db = json_service.get_database()
    for i, elem in enumerate(db["medicaments"]):
        if elem["id"] == id:
            db["medicaments"][i]["count"] += count
    json_service.set_database(db)