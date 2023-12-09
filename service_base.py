def IsInt():
    flag = True
    while flag:
        try:
            value = int(input())
            flag = False
        except:
            print('Попробуйте ещё раз!')
    return value

def IsInt_length(length=-1):
    flag = True
    while flag:
        try:
            value = int(input())
            if length != -1 and len(str(value)) == length:
                flag = False
                print('Win')
            else:
                print(f'Ограничение на количество символов: {length}')
        except:
            print('Неверный формат введённых данных')