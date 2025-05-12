# создание множества
# my_set = {1, 2, 3}
# print(my_set)
#
# создание пустого множества
# empty_set = set()
# print(empty_set)

# создание множества из другого набора элементов
# fruits = ["яблоко", "банан", "вишня", "яблоко"]
# fruits_set = set(fruits)
# print(fruits_set)

# скопировать содержимое множества
# fruits = ["яблоко", "банан", "вишня", "яблоко"]
# fruits_set = set(fruits)
# fruits_set2 = fruits_set.copy()
# print(fruits_set2)


# уникальность значений множества
# my_set = {4, 5, 2, 2}
# print(my_set) # {2, 4, 5}

# sec_set = {'a', 'd', [2, 5, 6]}
# print(sec_set) # TypeError


# получить и удалить случайный элемент
# my_set = {1, 2, 3, 4}
# element = my_set.pop()
# print(element)  # Случайный элемент
# print(my_set)   # Оставшиеся элементы


# add() - добавление элемента в множество
# my_set = {1, 2, 3}
# my_set.add(4)
# print(my_set)  # Вывод: {1, 2, 3, 4}

# Попытка добавить дубликат
# my_set.add(2)
# print(my_set)  # Вывод: {1, 2, 3, 4} (без изменений)


# удаление элемента
# my_set = {1, 2, 3}
# Удаление с remove()
# my_set.remove(2)
# print(my_set)  # Вывод: {1, 3}

# # Удаление с discard()
# my_set.discard(4)  # Ошибки нет, хотя 4 не в множестве
# print(my_set)

# # Удаление случайного элемента с pop()
# removed = my_set.pop()
# print(removed)  # Вывод: 1 или 3 (случайно)
# print(my_set)   # Оставшиеся элементы

# # Очистка множества
# my_set.clear()
# print(my_set)  # Вывод: set()


#new_set = {'a', 'b', 'c', 'd'}
# new_set.add('e')
# print(new_set)
# new_set.add('a')
# print(new_set)
# new_set.remove('f')
# print(new_set)
# new_set.discard('f')
# print(new_set)
# new_set.pop()
# print(new_set)


# len
#my_set = {1, 2, 3}
#print(len(my_set))


# объединение множеств
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set1 | set2
# print(union_set)

# union_sets = set1.union(set2)
# print(union_sets)


# пересечение можеств
# yulka = {'Ylka', '25', 'Kazan'}
# pashka = {'Pashka', '25', 'Spb'}
# fam = yulka.union(pashka)
# print(fam)
# intersection_fam = yulka & pashka
# intersection_fam2 = yulka.intersection(pashka)
# print(intersection_fam)
# print(intersection_fam2)


# разность множеств
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# difference_set = set1 - set2
# print(difference_set)
# difference_set1 = set1.difference(set2)
# print(difference_set1)


# симметрическая разность множеств
# sett1 = {1, 2, 3}
# sett2 = {3, 4, 5}
# symmetric_diff = sett1 ^ sett2
# print(symmetric_diff)
# symmetric_diff2 = sett1.symmetric_difference(sett2)
# print(symmetric_diff2)


# сравнение множеств

#set1 = {1, 2}
#set2 = {1, 2, 3}

# Проверка подмножества
#print(set1 < set2)   # True: set1 строго подмножество set2
#print(set1 <= set2)  # True: set1 подмножество set2
#print(set1.issubset(set2)) # True

# Проверка надмножества
#print(set2 > set1)   # True: set2 строго надмножество set1
#print(set2 >= set1)  # True: set2 надмножество set1
#print(set2.issuperset(set1)) # True

#равные множества
#set1 = {1, 2, 3}
#set2 = {3, 2, 1}

#print(set1 == set2)  # True: элементы одинаковые
#print(set1 <= set2)  # True: set1 подмножество set2
#print(set1 >= set2)  # True: set1 надмножество set2
#print(set1 < set2)   # False: set1 не строго подмножество set2


# list1 = [10, 20, 30, 40, 50]
# list2 = [20, 25, 30, 35, 40]
# set1 = set(list1)
# set2 = set(list2)
# a = set1 - set2
# a_res = list(a)
# print(a_res)
#
# b = set1 | set2
# b_res = list(b)
# print(b_res)
#
# c = set1.intersection(set2)
# c_res = list(c)
# print(c_res)


# проверка наличия элемента
setin = {'a', 'b', 'c', 'f'}
print('a' in setin) # True
print('e' in setin) # False