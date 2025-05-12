#if-else 1
# num = int(input('Введите число: '))
# if num % 2 == 0:
#     print('Число четное')
# else:
#     print('Число нечетное')


# #if-else 2
# n = 2
# sum = 3000
# res = n * sum
# if res > 10000:
#     print(res * 0.8)
# elif res > 5000:
#     print(res * 0.9)
# else:
#     print(res)


#if-else 3
# pas = input('Введите пароль: ')
# if pas == 'qwerty123':
#     print('Доступ разрешен')
# elif pas == '':
#     print('Нужен пароль')
# else:
#     print('Пароль неверный')


#list 1
# lst = [1, 2, 3, 4, 5]
# print(sum(lst))


#list 2
# nums = [3, 4, 11 ,4 ,4]
# nums[2] = 100
# print(nums)


#list 3
# lst = []
# r = range(1, 100, 3)
# lst.append(list((r)))
# print(lst)


#dict 1
# menu = {'тар-тар': '800', 'минестроне': '550', 'тирамису': '700'}
# menu['карпачо'] = '1500'
# print(menu)
# menu['карпачо'] = '1100'
# print(menu)


#dict 2
# products = {'яблоко': 100, 'банан': 50, 'апельсин': 70}
# order = 'яблоко'
# if order in products:
#     print(products[order])
# else:
#     print('У нас нет такого товара')


#for 1
# r = range(1, 6)
# for i in r:
#     print(i ** 2)


#for 2.1
# n = int(input('Введите число больше единицы: ')) + 1
# r = range(1, n)
# print(sum(r))


#for 2.2
# n = int(input('Введите число больше единицы: ')) + 1
# r = range(1, n)
# res = 0
# for i in r:
#     res += i
# print(res)


#for 3
# r = range(10, 0, -1)
# for i in r:
#     print(i)


#for 4
# fruits = ["яблоко", "банан", "груша"]
# for e in fruits:
#     print(e)


#for 5.1 - найти максимальное число
# numbers = [3, 8, 1, 9, 4]
# max = numbers[0
# a = 0
# for i in numbers:
#     if numbers[a] > max:
#         max = i
#     a += 1
# print(max)


# найти минимальное число
# numbers = [3, 8, 1, 9, 4]
# min = numbers[0]
# a = 0
# for i in numbers:
#     if numbers[a] < min:
#         min = i
#     a += 1
# print(min)


# enumerate
numbers = [3, 8, 1, 9, 4]
min = numbers[0]
for index, element in enumerate(numbers):
    if numbers[index] < min:
        min = element
#print(min)


#for 5.2 - максимальное через сортировку
# numbers = [3, 8, 1, 9, 4]
# numbers.sort()
# print(numbers[-1])
# print(max(numbers)) # проверить


#for 6.1
# products = {"яблоко": 100, "банан": 50, "апельсин": 70}
# print(sum(products.values()))


#for 6.2
# products = {"яблоко": 100, "банан": 50, "апельсин": 70}
# res = 0
# for name, price in products.items():
#     res += price
# print(res)


#while 1
# x = 1
# while x <= 10:
#     print(x)
#     x += 1


#while 2
# n = int(input('Введите число больше единицы: '))
# x = 1
# res = 0
# while x <= n:
#     res += x
#     x += 1
# print(res)


#while 3.1 - через for
# nums = [2, 7, 4, 9, 6, 5]
# for n in nums:
#     if n % 2 == 0:
#         nums.pop(nums.index(n))
# print(nums)


#while 3.2
# nums = [2, 7, 4, 9, 6, 5]
#
# res = []
# index = 0
# while index < len(nums):
#     if nums[index] % 2 == 1:
#         res.append(nums[index])
#     index += 1
# nums = res
# print(nums)

#while 3.3
# nums = [2, 7, 4, 9, 6, 5]
#
# index = 0
# while index < len(nums):
#     if nums[index] % 2 == 0:
#         nums.remove(nums[index])
#         index -=1
#     index += 1
# print(nums)


#mutable datas
# a = [1, 2, 3]
# b = a.copy()
# b[0] = 4
# print(a)
# print(b)
# print(id(a))
# print(id(b))


time = 3661

hours = time // 3600
minutes = (time % 3600) // 60
sec = (time - (hours * 3600) - (minutes * 60))

if hours == 1:
    h_text = 'час'
elif hours in range(2,5):
    h_text = 'часа'
else:
    h_text = 'часов'

if minutes == 1:
    m_text = 'минута'
elif minutes in range(2,5):
    m_text = 'минуты'
else:
    m_text = 'минут'

if sec == 1:
    s_text = 'секунда'
elif sec in range(2,5):
    s_text = 'секунды'
else:
    s_text = 'секунд'

print(f'{hours} {h_text} {minutes} {m_text} {sec} {s_text}')
print(str(hours) + ' ' + h_text + ' ' + str(minutes) + ' ' + m_text + ' ' + str(sec) + ' ' + s_text)