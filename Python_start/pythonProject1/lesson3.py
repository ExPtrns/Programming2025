# # Задание 1. Удаление дубликатов из списка
# # Дан список повторяющихся элементов. Вернуть список с дублирующимися
# # элементами. В результирующем списке не должно быть дубликатов.
#
# elements = [1, 2, 2, 3, 4, 4, 4, 5, 5]
#
# duplicates = []
# for i in elements:
#     if elements.count(i) > 1 and i not in duplicates:
#         duplicates.append(i)
# print(duplicates)
import random


# Задача 2. Поиск наибольшего числа в списке
# Напишите программу, которая принимает список чисел через строку и
# возвращает наибольшее число в этом списке.
# numbers = map(int, input("Enter the numbers separated by space: ").split(" "))
# print(max(numbers))


# Задача 3. Проверка палиндрома
# Напишите программу, которая принимает строку и определяет, является ли она
# палиндромом (читается одинаково с обеих сторон).
# some_string = input("Enter the string: ").lower()
# new_string = ''
# for letter in some_string:
#     if letter.isalpha():
#         if letter == 'ё':
#             letter = 'е'
#         new_string += letter
# palindrome = True
# for i in range((len(new_string)-1)//2):
#     if new_string[i] != new_string[len(new_string)-i-1]:
#         palindrome = False
# if palindrome:
#     print('Строка является палиндромом')
# else:
#     print('Строка не является палиндромом')

# Задача 4. Генерация паролей
# Напишите программу, которая генерирует случайный пароль заданной длины,
# состоящий из букв, цифр и специальных символов.
# pass_length = int(input("Enter a password length: "))
# symbols = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*_'
# password = ''
# for _ in range(pass_length):
#     password += random.choice(symbols)
# print(password)

# Задача 5. Нахождение анаграмм
# Напишите программу, которая принимает два слова и определяет, являются ли
# они анаграммами.
# first_word = input('Enter a word: ').lower()
# second_word = input('Enter another word: ').lower()
# if len(first_word) != len(second_word):
#     print('The words is not anagram')
# if sorted(first_word) == sorted(second_word):
#     print('The word is anagram')
# else:
#     print('The word is not anagram')
