# Задание 1. Функцию группового переименования файлов.
# Напишите функцию группового переименования файлов. Она должна:
# 1. принимать параметр желаемое конечное имя файлов. При
# переименовании в конце имени добавляется порядковый номер.
# 2. принимать параметр количество цифр в порядковом номере.
# 3. принимать параметр расширение исходного файла. Переименование
# должно работать только для этих файлов внутри каталога.
# 4. принимать параметр расширение конечного файла.
# 5. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик
# файлов и расширение. 3.Соберите из созданных на уроке и в рамках домашнего
# задания функций пакет для работы с файлами.
import os
import time
import zipfile


#
#
# # directory, wanted_names, count_numbers, old_extention, new_extention, old_name_part
# def group_files_rename(directory, new_extention, wanted_names='new_file', count_numbers=1, old_extention='*',  old_name_part=None):
#     os.chdir(f'{directory}')
#     print(f'Before - {os.listdir()}')
#     if not os.path.exists(directory):
#         raise FileNotFoundError(f"Каталог '{directory}' не найден.")
#     if old_extention == '*':
#         files = (file for file in os.listdir() if not os.path.isdir(file))
#     else:
#         files = (file for file in os.listdir() if file.endswith(f'.{old_extention}') and not os.path.isdir(file))
#     format_numbers = f'{{:0{count_numbers}d}}'
#     for index, file in enumerate(files, start=1):
#         if old_name_part is not None:
#             first_symb, last_symb = old_name_part.split('-')
#             old_part = f'_{file[int(first_symb):int(last_symb)+1]}'
#         else:
#             old_part = ''
#         print(old_part)
#         try:
#             os.rename(file, f"{old_part}{wanted_names}_{format_numbers.format(index)}.{new_extention}")
#         except FileExistsError:
#             os.rename(file, f"{old_part}{wanted_names}_{format_numbers.format(index)}(1).{new_extention}")
#
#     print(f'After - {os.listdir()}')
#
#
# group_files_rename('D://test', 'txt', 'renamed_file', 1, '*')
# Задача 2. Создание архива каталога
# Напишите скрипт, который создает архив каталога в формате .zip. Скрипт
# должен принимать путь к исходному каталогу и путь к целевому архиву. Архив
# должен включать все файлы и подпапки исходного каталога.

# def make_zip(directory_from, directory_to):
#     with zipfile.ZipFile(directory_to, 'w', zipfile.ZIP_DEFLATED) as zipf:
#         for root, dirs, files in os.walk(directory_from):
#             for file in files:
#                 file_path = os.path.join(root, file)
#                 zipf.write(file_path, os.path.relpath(file_path, directory_from))
#         return f'Successfully archived in {zipf.filename}'
#
#
# print(make_zip('D://test/1', 'D://test/new.zip'))
#
# Задача 3. Удаление старых файлов
# Напишите скрипт, который удаляет файлы в указанном каталоге, которые не
# изменялись более заданного количества дней. Скрипт должен принимать путь к
# каталогу и количество дней.

# def delete_old_files(directory, days=365):
#     today = time.time()
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             file_path = os.path.join(root, file)
#             # print(f'{root}{file} updated {int(round((today - os.path.getmtime(file_path)) / 86400,0))} days ago.')
#             if int(round((today - os.path.getmtime(file_path)) / 86400, 0)) > days:
#                 os.remove(file_path)
#                 print('Deleted old file: {}'.format(file_path))
#
#
#
# delete_old_files('D://test', 10)
# Задача 4. Поиск файлов по расширению
# Напишите функцию, которая находит и перечисляет все файлы с заданным
# расширением в указанном каталоге и всех его подкаталогах. Функция должна
# принимать путь к каталогу и расширение файла.
# def find_files(directory, extention):
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.endswith(extention):
#                 file_path = os.path.join(root, file)
#                 print(file_path)
#
# find_files('D:\\test', '.pdf')