from functional import create
from interface import interface

path = "phone_book.txt"
create(path)
enter = 0
while enter != 6:
     enter = interface()
     if enter == 1:
        from functional import add_cont
        stroka = str(input("Введите ФИО и номер телефона через пробел "))
        add_cont(path, stroka)
     elif enter == 2:
        from functional import show_all
        print(show_all(path))
     elif enter == 3:
        from functional import search
        stroka = str(input("Введите фамилию:    "))
        search(path, stroka)
     elif enter == 4:
        from functional import deletion
        stroka = str(input("Введите фамилию"))
        deletion(path, stroka)
     elif enter == 5:
        from functional import change_contact
        stroka = str(input("Введите фамилию"))
        change_contact(path, stroka)
print("спасибо за работу")
