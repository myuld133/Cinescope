# dict1 = {'name': 'Alice', 'age': '5'}
# dict2 = dict1.copy()
# print(dict2)


# my_dict = {
# 	"name": "Alice",
# 	"age": 25,
# 	"city": "Phuket"
# 	}
#
# # Получение значения по ключу
# print(my_dict["name"])  # Вывод: Alice
# print(my_dict["age"])   # Вывод: 25


# my_dict = {"name": "Alice", "age": 25}
#
# # Добавление нового элемента
# my_dict["city"] = "New York"
# print(my_dict)  # Вывод: {'name': 'Alice', 'age': 25, 'city': 'New York'}


# my_dict = {"name": "Alice", "age": 25, "city": "New York"}
#
# # pop
# removed_value = my_dict.pop("age")
# print(removed_value)  # Вывод: 25
# print(my_dict)        # Вывод: {'name': 'Alice', 'city': 'New York'}
#
# # del
# del my_dict["city"]
# print(my_dict)  # Вывод: {'name': 'Alice'}
#
# # clear
# my_dict.clear()
# print(my_dict)  # Вывод: {}


# объединение словарей
# dict1 = {"name": "Alice", "age": 25}
# dict2 = {"city": "New York", "age": 30}
#
# result = dict1 | dict2
# print(result)


# dict1 = {"name": "Alice", "age": 25}
# dict2 = {"city": "New York", "age": 30}
#
# dict1.update(dict2)
# print(dict1)  # Вывод: {'name': 'Alice', 'age': 30, 'city': 'New York'}


# users = {
#     "Alice": {
#         "phone": "+971478745",
#         "email": "alice12@gmail.com"
#     },
#     "Bob": {
#         "phone": "+876390444",
#         "email": "bob@gmail.com",
#         "skype": "bob123"
#     }
# }
#
# extracted_email = users["Alice"]["email"]
# print(extracted_email)  # alice12@gmail.com


# my_datas = {'name': 'Yulka', 'age': '24', 'married': 'True'}
# new_datas = my_datas.copy()
# assert my_datas == new_datas, 'Ожидается, что my_datas совпадает с new_datas'
# #print(new_datas)
#
# my_datas['phone'] = '89857297140'
# #print(my_datas)
#
# my_datas['phone'] = '898******40'
# #print(my_datas)
#
# residence = {
#     'residence': {
#         'country': 'Russia',
#         'city': 'spb',
#         'district': 'Parnas'
#     }
# }
#
# my_datas.update(residence)
# print(my_datas.keys())
#
# print(my_datas['residence']['city'])


# проверка наличия элемента
dictin = {'Monday': 'sunny', 'Thuersday': 'windy', 'Wednesday': 'rainy'}
print('Monday' in dictin) # True
print('Friday' in dictin) # False