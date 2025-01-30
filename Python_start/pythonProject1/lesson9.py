import time
from functools import wraps


#
#
# def how_are_you(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         input('Hello, how_are_you?\n')
#         print("And I'm not good")
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @how_are_you
# def bigger_number(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2
#
#
# print(bigger_number(2, 3))
# Задача 2. Замедление кода
# В программировании иногда возникает ситуация, когда работу функции нужно
# замедлить. Типичный пример — функция, которая постоянно проверяет,
# изменились ли данные на веб-странице или её код.
# Реализуйте декоратор, который перед выполнением декорируемой функции
# ждёт несколько секунд.

# def slowdown(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         time.sleep(2)
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @slowdown
# def bigger_number(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2
#
#
# print(bigger_number(1, 2))
# Задача 3. Счётчик
# Реализуйте декоратор counter, считающий и выводящий количество вызовов
# декорируемой функции.
# Для решения задачи нельзя использовать операторы global и nonlocal.

# def counter(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         wrapper.count += 1
#         result = func(*args, **kwargs)
#         print(f'Функция {func.__name__} вызвана {wrapper.count} раз.')
#         return result
#     wrapper.count = 0
#     return wrapper
#
#
# @counter
# def bigger_number(num1, num2):
#     return f'Большее число из {num1} и {num2} - {max(num1, num2)}'
