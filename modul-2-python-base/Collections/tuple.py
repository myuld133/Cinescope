# создание кортежа

# my_tuple = (1, 2, 3)
# print(my_tuple)

# my_tuple = 1, 2, 3
# print(my_tuple)

# my_tuple = (1,)
# print(type(my_tuple))

# empty_tuple = ()
# print(empty_tuple)

# numbers_list = [1, 2, 3, 4]
# numbers_tuple = tuple(numbers_list)
# print(type(numbers_tuple))


# неизменяемость кортежей
# my_tuple = (1, 4, 6)
# my_tuple[1] = 10 # TypeError


# обратиться по индексу
# new_tuple = ('a', 'v', 's', 'r')
# print(new_tuple[0])


# сравнение кортежей
# tuple1 = ({"object": "in_tuple"}, 2, 'a')
# tuple2 = tuple(tuple1)
# assert tuple1 == tuple2, f'кортеж {tuple1} не равен {tuple2}'
# print(tuple1 == tuple2)


# len - узнать длину кортежа
# my_tuple = (1, 2, 3, 4)
# print(len(my_tuple))


# распаковка кортежа
# coordinates = (10, 20)
# x, y = coordinates  # Распаковываем кортеж
# print(x)
# print(y)

# values = (1, 2, 3, 4, 5)
# a, b, *rest = values
# print(a)
# print(b)
# print(rest)  # Вывод: [3, 4, 5]


# конкатенация
# tuple1 = ({"object": "in_tuple"}, 2)
# tuple2 = (3, ["слон", 1, True])
# combined = tuple1 + tuple2
# print(combined)
# print(combined[3][0])


# получение индекса
# my_tuple = (10, 20, 30)
# print(my_tuple.index(20))
#
# # получение количества
# my_tuple = (1, 2, 3, 3)
# print(my_tuple.count(3))


fruits = ("apple", "banana", "cherry", "apple")
# print(fruits.index('apple'))
#print(fruits.count('apple'))

a, b, *rest = fruits
# print(a)
# print(b)
# print(rest)

tuple_2 = tuple(rest)
#
# assert len(tuple_2) == 2, f'Длина {tuple_2} не 2'
# print('True')


# проверка наличия элемента
tuplein = (2, 5, 3, 4, 10)
print(2 in tuplein) # True
print(0 in tuplein) # False