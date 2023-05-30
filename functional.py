def create(path):
        try:
            file = open(path, 'r')
        except IOError:
            print('Создан новый справочник -> phone_book.txt ')
            file = open(path, 'w')
        finally:
            file.close()

def add_cont(file_name, stroka):
        data = open(file_name, 'a')
        data.write(stroka + "\n")
        data.close()


def show_all(file_name):
    data = open(file_name, "r", encoding='utf-8')
    for line in data:
        print(line[:-1])
    data.close()

def search(file_name, stroka):
        a = 0
        data = open(file_name, 'r')
        for line in data:
            if stroka in line:
                print(line)
                a = 123
                break
        if a != 123:
            print("нет такого")
        data.close()


def deletion(file_name, del_name):
    data = open(file_name, 'r', encoding='utf-8')
    list_name = list()
    for line in data:
        if del_name in line:
            stroka = line
            continue
        if line != "": list_name.append(line)
    data.close()

    list_name = list(filter(lambda x: x != "", list_name))

    data = open(file_name, 'w', encoding='utf-8')
    for item in list_name:
        data.write(item)

        data.close()

        print(f" Контакт: {stroka} >>удален<< \n")


def change_contact(file_name, ch_name):
    data = open(file_name, 'r', encoding='utf-8')
    list_name = list()
    for line in data:
        if ch_name in line:
            new_name = input("Введите новое Ф.И.О. и номер")

            list_name.append(new_name + "\n")
            continue
            list_name.append(line)
        data.close()

    list_name = list(filter(lambda x: x != "", list_name))
    data = open(file_name, 'w', encoding='utf-8')

    for item in list_name:
        data.write(item)
        data.close()
        print()
