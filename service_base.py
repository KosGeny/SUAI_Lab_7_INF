def IsInt():
    flag = True
    while flag:
        try:
            value = int(input())
            flag = False
        except:
            print('Попробуйте ещё раз!')
    return value

def IsInt_length(length):
    flag = True
    while flag:
        try:
            value = int(input())
            if len(str(value)) == length:
                flag = False
            else:
                print(f'Ограничение на количество символов: {length}')
        except:
            print('Неверный формат введённых данных')
    return value

def IsInt_Range(range):
    flag = True
    while flag:
        try:
            value = int(input())
            if value in range:
                flag = False
            else:
                print('Число не соответсвует списку допустимых значений')
        except:
            print('Неверный формат введённых данных')
    return value