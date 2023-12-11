import utils.json_service as json_service

def selling(id):
    db = json_service.get_database()
    while True:
        try:
            value = int(input('Количество: '))
            if value > 0:
                for i, elem in enumerate(db["medicaments"]):
                    if elem["id"] == id:
                        if elem["count"] >= value:
                            db["medicaments"][i]["count"] -= value
                            income = elem["price"]*value
                            json_service.set_database(db)
                            return value, income
                        else:
                            print('Превышение количества')
            else:
                print('Количество должно быть больше нуля!')
        except:
            print('Ой, что-то пошло нет так! Попробуйте ещё раз!')

def refund(id, count):
    db = json_service.get_database()
    for i, elem in enumerate(db["medicaments"]):
        if elem["id"] == id:
            db["medicaments"][i]["count"] += count
    json_service.set_database(db)