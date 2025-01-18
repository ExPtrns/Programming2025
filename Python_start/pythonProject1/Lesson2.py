# Задача 1. Нахождение наибольшего общего делителя (НОД) двух
# чисел
# Программа принимает два целых числа и находит их наибольший общий
# делитель (НОД).
#
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# while b:
#     a, b = b, a % b
# print(a)
#
# Задание 2. Преобразование числа в шестнадцатеричное
# представление
# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте для
# проверки своего результата.
#
# num = int(input("Enter a number: "))
# hex_sym = '0123456789ABCDEF'
# result = ''
# sign = ''
# if num == 0:
#     print(num)
# if num < 0:
#     num = -num
#     sign += '-'
# while num > 0:
#     result = hex_sym[num % 16] + result
#     num //= 16
# print(f'{sign}{result}')


# Задача 3. Перевод целого числа в римское число
# Программа принимает целое число и возвращает его римское представление в
# виде строки.

# def print_roman(number):
#     num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
#     sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
#     i = 12
#
#     while number:
#         div = number // num[i]
#         number %= num[i]
#
#         while div:
#             print(sym[i], end="")
#             div -= 1
#         i -= 1
#
#     numb = int(input("Enter a number: "))
#     print("Roman number is:", end=" ")
#     print_roman(numb)
#

# Задача 4. Сумма и произведение дробей
# Программа принимает две строки вида "a/b" - дробь с числителем и
# знаменателем. Возвращает сумму и произведение дробей. Для проверки
# используется модуль fractions.
#
# def get_nok(d1, d2):
#     result = 1
#     first_divs, second_divs = [], []
#     while d1 > 1:
#         for i in range(2, d1 + 1):
#             if d1 % i == 0:
#                 first_divs.append(i)
#                 d1 = int(d1 / i)
#                 break
#     while d2 > 1:
#         for i in range(2, d2 + 1):
#             if d2 % i == 0:
#                 second_divs.append(i)
#                 d2 = int(d2 / i)
#                 break
#     for i in first_divs:
#         result *= i
#         if i in second_divs:
#             second_divs.remove(i)
#     for i in second_divs:
#         result *= i
#     return result
#
# def get_sum(numerator1,denominator1, numerator2, denominator2):
#     if denominator1 != denominator2:
#         gen_denom = get_nok(denominator1, denominator2)
#         numerator1 = int(gen_denom / denominator1 * numerator1)
#         numerator2 = int(gen_denom / denominator2 * numerator2)
#         gen_num = numerator1 + numerator2
#         return gen_num/gen_denom
#
# def get_mult(numerator1,denominator1,numerator2,denominator2):
#     return (numerator1 * numerator2)/(denominator1 * denominator2)
#
#
# first_frac = input("Enter first fraction: ")
# numerator1, denominator1 = map(int, first_frac.split('/'))
# second_frac = input("Enter second fraction: ")
# numerator2, denominator2 = map(int, second_frac.split('/'))
#
# sum_fract = get_sum(numerator1, denominator1, numerator2, denominator2)
# mult_fract = get_mult(numerator1, denominator1, numerator2, denominator2)
#
# print(f'{numerator1} / {denominator1} + {numerator2} / {denominator2} = {sum_fract}')
# print(f'{numerator1} / {denominator1} * {numerator2} / {denominator2} = {mult_fract}')
