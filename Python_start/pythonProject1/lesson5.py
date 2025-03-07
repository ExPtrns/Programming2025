# Задание 1. Квадраты чисел
# Пользователь вводит число N. Напишите программу, которая генерирует
# последовательность из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так
# далее). Реализацию напишите двумя способами: функция-генератор и
# генераторное выражение.
# def get_all_sqares(n):
#     for i in range(1, n + 1):
#         print(i ** 2, end=' ')
#     print()
#
#
# number = int(input("Enter a number: "))
# get_all_sqares(number)
# gen_squares = (i ** 2 for i in range(1, number + 1))
# for i in gen_squares:
#     print(i, end=' ')

# Задача 2. Однострочный генератор словаря
# Напишите однострочный генератор словаря, который принимает на вход три
# списка одинаковой длины: имена str, ставка int, премия str с указанием
# процентов вида 10.25%.
# В результате result получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.
# Не забудьте распечатать в конце результат.
# Пример использования.
# На входе:
# names = ["Alice", "Bob", "Charlie"]
# salary = [5000, 6000, 7000]
# bonus = ["10%", "5%", "15%"]
# На выходе:
# {'Alice': 500.0, 'Bob': 300.0, 'Charlie': 1050.0}

# names = ["Alice", "Bob", "Charlie"]
# salary = [5000, 6000, 7000]
# bonus = ["10%", "5%", "15%"]
# int_bonus = [int(i.split('%')[0])*0.01 for i in bonus]
# prem = {}
#
#
# for i in range(len(names)):
#     prem[names[i]] = salary[i] * int_bonus[i]
# print(prem)
#
# Задача 3. Генератор последовательности чисел Фибоначчи
# Напишите генераторную функцию fibonacci(n), которая принимает на вход
# одно целое число n и возвращает последовательность первых n чисел
# Фибоначчи. Числа Фибоначчи — это последовательность, в которой каждое
# число является суммой двух предыдущих, начиная с 0 и 1.
# def fibonacci(n):
#     x, y = 0, 1
#
#     for _ in range(n):
#         yield x
#         x, y = y, x + y
#
#
# number = int(input('Enter a number: '))
# for number in fibonacci(number):
#     print(number)

# Задача 4. Генератор подстрок
# Напишите генераторную функцию substrings(s), которая принимает строку
# s и возвращает генератор всех возможных подстрок этой строки.
# На вход подается строка abc
# На выходе будут выведены обозначения:
# a
# ab
# abc
# b
# bc
# c

# def substrings(s):
#     for start in range(len(s)):
#         for end in range(start + 1, len(s) + 1):
#             yield s[start:end]
#
# for substring in substrings('abc8'):
#     print(substring)
