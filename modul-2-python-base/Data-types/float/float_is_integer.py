# number1 = 10.0
# number2 = 10.5
# is_whole_number1 = number1.is_integer()
# print(is_whole_number1)
# is_whole_number2 = number2.is_integer()
# print(is_whole_number2)


num = float(input("Введите число: "))
res = num.is_integer()
if res == True:
    print('Число целое')
else:
    print('Число не является целым')