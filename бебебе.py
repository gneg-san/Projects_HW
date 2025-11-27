# 1.
'''
num1 = int(input("Введите число: "))
num2 = int(input("Введите число: "))
num3 = int(input("Введите число: "))
user_choice = int(input("1- сумма чисел, 2 - произведение чисел "))
if user_choice == 1:
    print(num1 + num2 + num3)
elif user_choice == 2:
    print(num1 * num2 * num3)
else:
    print()
'''
# 2.
'''
num1 = int(input("Введите число: "))
num2 = int(input("Введите число: "))
num3 = int(input("Введите число: "))
user_choice = int(input("1- наибольшее число, 2 - наименьшее число, 3 - среднее арифметическое "))
if user_choice == 1:
    print()
elif user_choice == 2:
    print()
elif user_choice == 3:
    print((num1 + num2 + num3) / 3)
else:
    print()
'''
# 3.
'''
value = int(input("Введите ко-во метров: "))
user_choice = ("1 - перевести в мили, 2 - перевести в дюймы, 3 - перевести в ярды ")
if user_choice == 1:
    print(value * 0.000621)
elif user_choice == 2:
    print(value * 39.37)
elif user_choice == 3:
    print(value * 1.09)
else:
    print()
'''