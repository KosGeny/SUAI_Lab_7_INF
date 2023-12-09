def IsInt():
    flag = True
    while flag:
        try:
            value = int(input())
            flag = False
            print('Win')
        except:
            print('ijrjgirg')
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
                print('again')
        except:
            print('ijrjgirg')