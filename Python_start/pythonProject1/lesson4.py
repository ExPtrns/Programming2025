# Задание 1. Апгрейд калькулятора
# Степан использует калькулятор для расчёта суммы и разности чисел, но на
# работе ему требуются не только обычные арифметические действия. Он ничего
# не хочет делать вручную, поэтому решил немного расширить функционал
# калькулятора.
# Напишите программу, запрашивающую у пользователя число и действие,
# которое нужно сделать с числом: вывести сумму его цифр, максимальную или
# минимальную цифру. Каждое действие оформите в виде отдельной функции, а
# основную программу зациклите.
# Запрошенные числа должны передаваться в функции суммы, максимума и
# минимума при помощи аргументов.
# def summ_dig(number):
#     result = 0
#     numbers = []
#     for i in str(number):
#         numbers.append(int(i))
#     for i in numbers:
#         result += i
#     return result
#
#
# def min_dig(number):
#     numbers = []
#     for i in str(number):
#         numbers.append(int(i))
#     return min(numbers)
#
#
# def max_dig(number):
#     numbers = []
#     for i in str(number):
#         numbers.append(int(i))
#     return max(numbers)
#
#
# while True:
#     number = int(input('Enter a number: '))
#     choice = input(f'Choose an action:\n1 - To get the summ of digits in number {number},\n'
#                    f'2 - To get the minimal of digits in {number},\n'
#                    f'3 - To get the maximal of digits in {number},\n'
#                    f'Exit - To exit the program.\n').strip().lower()
#     if choice == '1':
#         print(f'The summ of digits in number {number} = {summ_dig(number)}.')
#     elif choice == '2':
#         print(f'The minimal of digits in {number} = {min_dig(number)}.')
#     elif choice == '3':
#         print(f'The maximal of digits in {number} = {max_dig(number)}.')
#     elif choice == 'exit':
#         break
#     else:
#         print('Invalid input')
# Задача 2. Недоделка
# Вы пришли на работу в компанию по разработке игр, целевая аудитория —
# дети и их родители. У предыдущего программиста было задание сделать две
# игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# Однако программист, на место которого вы пришли, перед увольнением не
# успел выполнить эту задачу и оставил только небольшой шаблон проекта.
# Используя этот шаблон, реализуйте игры «Камень, ножницы, бумага» и «Угадай
# число».
# Правила игры «Камень, ножницы, бумага»: программа запрашивает у
# пользователя строку и выводит, победил он или проиграл. Камень бьёт
# ножницы, ножницы режут бумагу, бумага кроет камень.
# Правила игры «Угадай число»: программа запрашивает у пользователя число
# до тех пор, пока он не отгадает загаданное.
# import random
#
#
# def rock_paper_scissors():
#     print('Welcome to Rock Paper Scissors!')
#     variants = ['rock', 'paper', 'scissors']
#     options = {
#         'rock': 'scissors',
#         'scissors': 'paper',
#         'paper': 'rock'
#     }
#     while True:
#         pc_choice = random.choice(variants)
#         player_choice = input('Make your choice (Rock Paper or Scissors or 0 to return Main menu): \n').lower()
#         if player_choice == '0':
#             break
#         if player_choice not in variants:
#             print('Sorry, you have entered an invalid option.')
#             continue
#         print(pc_choice)
#         if pc_choice == player_choice:
#             print("Tie")
#             continue
#         for i, j in options.items():
#             if pc_choice == i and player_choice == j:
#                 print("You loose!")
#                 break
#             elif player_choice == i and pc_choice == j:
#                 print("You win!")
#                 break
#
#
# def guess_the_number():
#     print('Welcome to Guess the number!')
#     game_range = int(input('Select a range for the game(from 1):\n'))
#     if game_range < 1:
#         return
#     pc_number = random.randint(1, game_range)
#     while True:
#         number = int(input(f'Guess a number from 1 to {game_range} or put "0" to exit the game: \n'))
#         if number == 0:
#             break
#         elif number == pc_number:
#             print("That's wright! You win!")
#             game_range = int(input('Select a range for the game(from 1):\n'))
#             continue
#         else:
#             print('Nice try, but you are wrong!')
#
#
# def main_menu():
#     print("Welcome to Main menu!")
#     while True:
#         print("[1] Rock Paper Scissors")
#         print("[2] Guess the Number")
#         print("[0] Exit")
#         option = input("Enter your choice: ")
#         if option == '1':
#             rock_paper_scissors()
#         elif option == '2':
#             guess_the_number()
#         elif option == '0':
#             print("Thank you for playing!")
#             break
#         else:
#             print("Please enter a valid option!")
#
#
# main_menu()
# Задача 3. Число наоборот
# Пользователь вводит два числа: N и K. Напишите программу, которая заменяет
# каждое число на число, которое получается из исходного записью его цифр в
# обратном порядке, затем складывает их, снова переворачивает и выводит
# ответ на экран.
from unittest import result


# def back_num(number):
#     result = ''
#     numbers = []
#     for i in str(number):
#         numbers.append(int(i))
#     for i in range(len(numbers) - 1, -1, -1):
#         result += str(numbers[i])
#     return result
#
#
# n = int(input("Enter a N-number: "))
# k = int(input("Enter a K-number: "))
#
#
# print(f'Первое число наоборот: {back_num(n)}')
# print(f'Второе число наоборот: {back_num(k)}')
# print(f'Сумма: {int(back_num(n)) + int(back_num(k))}')
# print(f'Сумма наоборот: {back_num(int(back_num(n)) + int(back_num(k)))}')

# Задача 4. Функция максимума
# Юра пишет различные полезные функции для Python, чтобы остальным
# программистам стало проще работать. Он захотел написать функцию, которая
# будет находить максимум из перечисленных чисел. Функция для нахождения
# максимума из двух чисел у него уже есть. Юра задумался: может быть, её
# можно как-то использовать для нахождения максимума уже от трёх чисел?
# Помогите Юре написать программу, которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.
# По итогу в программе должны быть реализованы две функции:
# 1. maximum_of_two — функция принимает два числа и возвращает одно
# (наибольшее из двух);
# 2. maximum_of_three — функция принимает три числа и возвращает одно
# (наибольшее из трёх); при этом она должна использовать для сравнений
# первую функцию maximum_of_two.
# def maximum_of_two(a, b):
#     return max(a, b)
#
#
# def maximum_of_three(a, b, c):
#     max1 = maximum_of_two(a, b)
#     return maximum_of_two(max1, c)
#
#
# print(maximum_of_three(2, 4, 8))
# Задача 5. Яйца
# В рамках программы колонизации Марса компания «Спейс Инжиниринг»
# вывела особую породу черепах, которые, по задумке, должны размножаться,
# откладывая яйца в марсианском грунте. Откладывать яйца слишком близко к
# поверхности опасно из-за радиации, а слишком глубоко — из-за давления
# грунта и недостатка кислорода. Вообще, факторов очень много, но
# специалисты проделали большую работу и предположили, что уровень
# опасности для черепашьих яиц рассчитывается по формуле: D = x^3 − 3x^2 −
# 12x + 10, где x — глубина кладки в метрах, а D — уровень опасности в
# условных единицах. Для тестирования гипотезы нужно взять пробу грунта на
# безопасной, согласно формуле, глубине.
# Напишите программу, находящую такое значение глубины х, при котором
# уровень опасности как можно более близок к нулю. На вход программе
# подаётся максимально допустимое отклонение уровня опасности от нуля, а
# программа должна рассчитать приблизительное значение х, удовлетворяющее
# этому отклонению. Известно, что глубина точно больше нуля и меньше четырёх
# метров. Обеспечьте контроль ввода.
# Пример:
# Введите максимально допустимый уровень опасности: 0.01
# Приблизительная глубина безопасной кладки: 0.732421875 м
# def get_current_danger(d):
#     return d ** 3 - 3 * d ** 2 - 12 * d + 10
# def find_safe_depth(danger_level):
#     min_depth = 0
#     max_depth = 4
#     middle_depth = (min_depth + max_depth) / 2
#     middle_danger = get_current_danger(middle_depth)
#
#     while abs(middle_danger) > danger_level:
#         if middle_danger > 0:
#             min_depth = middle_depth
#         else:
#             max_depth = middle_depth
#         middle_depth = (min_depth + max_depth) / 2
#         middle_danger = get_current_danger(middle_depth)
#     return middle_depth
#
#
# danger_level = float(input('Enter the maximum allowable danger level:\n'))
# if danger_level < 0:
#     print('The maximum allowable danger level must be greater than zero.')
# else:
#     print(find_safe_depth(danger_level))