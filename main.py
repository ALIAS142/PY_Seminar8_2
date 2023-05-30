# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# def deletion(file_name, del_name):
#     data = open(file_name, 'r')
#     list_name = list()
#     for line in data:
#         if del_name in line:
#             print_name = line
#             continue
#         if line != "": list_name.append(line)
#         data.close()
#
#     list_name = list(filter(lambda x: x != "", list_name))
#
#     data = open(file_name, 'w')
#     for item in list_name:
#         data.write(item)
#
#         data.close()
#
# print(f" Контакт: {print_name} >>удален<< \n")
#
#
# def change_contact(file_name, ch_name):
#     data = open(file_name, 'r')
#     list_name = list()
#     for line in data:
#         if ch_name in line:
#             new_name = input("Введите новое Ф.И.О. и номер")
#
#         list_name.append(new_name + "\n")
#         continue
#         list_name.append(line)
#     data.close()
#
#
# list_name = list(filter(lambda x: x != "", list_name))
# data = open(file_name, 'w')
# for item in list_name:
#     data.write(item)
# data.close()
#
# print()
