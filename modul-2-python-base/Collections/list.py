#создание списка
# fruits = ["яблоко", "банан", "вишня"]
# numbers = [1, 2, 3, 4]
# numbers1 = [] #создание пустого списка
# numbers2 = list() #создание пустого списка
# print(fruits)


#создание списка из существующего
# numbers1 = [1, 2, 3, 4, 5]
# numbers2 = numbers1.copy()  # копирование
# numbers3 = list(numbers1)  # создание на основе первого


#узнать длину списка
# len
# my_list = [1, 2, "крыша", False]
# length = len(my_list)
# print(length)


#добавление элемента
# append
# fruits = ["яблоко", "банан", "вишня"]
# fruits.append("апельсин")
# print(fruits)
#
# # insert
# fruits = ['банан', 'яблоко']
# fruits.insert(1, 'апельсин')
# print(fruits)
#
# # extend
# fruits = ['банан', 'яблоко']
# fruits.extend(['груша', 'апельсин', 'вишня'])
# print(fruits)


#получение индекса элемента
# index
# fruits = ['банан', 'яблоко', 'апельсин']
# index = fruits.index('апельсин')
# print(index)
#
# fruits = ['банан', 'яблоко', 'апельсин']
# index = fruits.index('такого элемента нет в списке')
# print(index) #ValueError


#удаление элементов
# remove
# fruits = ['банан', 'яблоко', 'апельсин']
# fruits.remove('банан')
# print(fruits)
#
# # clear
# fruits = ['банан', 'яблоко', 'апельсин']
# fruits.clear()
# print(fruits)
#
# # pop
# fruits = ['банан', 'яблоко', 'апельсин']
# pop = fruits.pop(0)
# print(fruits)
# print(pop)


# fruits = [
#     ["яблоко", "розовые"],
#     ["апельсин", "цитрусовые"],
#     ["ананас", "бромелиевые"]
# ]
#
# print(fruits[0])
# print(fruits[0][0])
# print(fruits[0][1])


# fruits = [
#     ["яблоко", "розовые"],
#     ["апельсин", "цитрусовые"],
#     ["ананас", "бромелиевые"]
# ]
#
# # создание вложенного списка
# new_fruit = list()
# new_fruit.append("банан")
# new_fruit.append("банановые")
# # добавление вложенного списка
# fruits.append(new_fruit)
#
# # print(fruits[-1])  # ["банан", "банановые"]
#
# # добавление во вложенный список
# fruits[-1].append("желтый")
#
# # print(fruits[-1])  # ["банан", "банановые", "желтый"]
#
# # удаление последнего элемента из вложенного списка
# fruits[-1].pop()
# # print(fruits[-1])  # ["банан", "банановые"]
#
# # удаление всего последнего вложенного списка
# fruits.pop(-1)


# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# # print(c)
# assert len(a) == len(b), f'Ожидается, что длина списка a равна длине списка b'
# print(len(a) == len(b))


# numbers = [10, 20, 40, 50]
# numbers.insert(2, 30)
# print(numbers)
# numbers.clear()
# print(numbers)


# my_list = [
#     [1, 2, 3],
#     ['a', 'b', 'c'],
#     [True, False]
# ]
# print(my_list[1].pop(1))
# print(my_list)
# last_item = my_list[0].pop()
# print(last_item)

# проверка наличия элемента
listin = [2, 5, 8, 0]
print(5 in listin) # True
print(7 in listin) # False