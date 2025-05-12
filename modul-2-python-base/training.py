# # students = ["Алексей", "Мария", "Иван", "Ольга", "Дмитрий"]
# # math_grades = [4, 5, 3, 4, 5]
# # physics_grades = [3, 4, 5, 3, 4]
# # informatics_grades = [5, 4, 3, 5, 3]
# #
# #
# # # вывод информации о студентах
# # i = 0
# # while i < len(students):
# #     print(f'Студент: {students[i]}, Математика: {math_grades[i]}, Физика: {physics_grades[i]}, Информатика: {informatics_grades[i]}')
# #     i += 1
# #
# #
# # # поиск отличников
# # i = 0
# # while i < len(students):
# #     if math_grades[i] >= 4 and physics_grades[i] >= 4 and informatics_grades[i] >= 4:
# #         print('Отличники: ', students[i])
# #     i += 1
# #
# #
# # # средний балл по каждому предмету
# # print('Средний балл по математике: ', sum(math_grades) / len(math_grades))
# # print('Средний балл по физике: ', sum(physics_grades) / len(physics_grades))
# # print('Средний балл по информатике: ', sum(informatics_grades) / len(informatics_grades))
# #
# #
# # # определение самого успешного студента
# # success_students = []
# # i = 0
# # while i < len(students):
# #     avg_st = (math_grades[i] + physics_grades[i] + informatics_grades[i]) / 3
# #     avg_st = round(avg_st, 1)
# #     success_students.append(avg_st)
# #     i +=1
# # founded_score = max(success_students)
# # el = success_students.index(founded_score)
# # print(students[el])
#
#
# text = 'Python — это высокоуровневый язык программирования. Python поддерживает несколько парадигм программирования. Python прост в изучении!'
# print(text)
#
# # подсчет слов
# text_list = text.split()
# print(text_list)
# print('Количество слов:', len(text_list) - 1)
#
# # поиск самого длинного слова
# max_len = 0
# for word in text_list:
#     word_len = len(word)
#     if word_len > max_len:
#         max_len = word_len
# print(max_len)
#
# # частота букв
# letter_counts = {}
# for char in text.lower():
#     if char.isalpha():  # проверяем, что это буква
#         if char in letter_counts:
#             letter_counts[char] += 1
#         else:
#             letter_counts[char] = 1
# print(letter_counts)
#
#
# # замена слова
# old_word = input('Введите слово, которое нужно заменить: ')
# new_word = input('Введите новое слово: ')
# print(text.replace(old_word, new_word))


# items = []
# while True:
#     product = input('Выберите товар. Для завершение введи "стоп": ')
#     if product == 'стоп':
#         break
#     elif product in items:
#         print('Товар уже в корзине')
#     else:
#         items.append(product)
# items.sort()
# print('Твоя корзина: ', items)

print(list(range(1,21)))