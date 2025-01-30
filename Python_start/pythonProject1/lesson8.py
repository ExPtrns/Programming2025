# Задание 1. Работа с основными данными
# Напишите функцию, которая получает на вход директорию и рекурсивно обходит
# её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и
# pickle. Для дочерних объектов указывайте родительскую директорию. Для
# каждого объекта укажите файл это или директория. Для файлов сохраните его
# размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
# файлов и директорий. Соберите из созданных на уроке и в рамках домашнего
# задания функций пакет для работы с файлами разных форматов.
# import csv
# import os
# import json
# import pickle
#
#
# def save_to_json(diction):
#     with open('result.json', 'w') as json_file:
#         json.dump(diction, json_file, indent=4)
#
#
# def save_to_csv(diction):
#     with open('result.csv', 'w', newline='') as csv_file:
#         writer = csv.DictWriter(csv_file, diction.keys())
#         writer.writeheader()
#         writer.writerow(diction)
#
#
# def save_to_pickle(diction):
#     with open('result.pkl', 'wb') as pickle_file:
#         pickle.dump(diction, pickle_file)
#
# def get_dir_size(directory_path):
#     for root, dirs, files in os.walk(directory_path):
#         size = 0
#         for file in files:
#             size += os.path.getsize(os.path.join(root, file))
#         return size
#
# def get_dir_info(directory):
#     directories_dict = {'name': [], 'path': [], 'size': [], 'type': [], 'parent': []}
#     for root, dirs, files in os.walk(directory):
#         info = root.split(os.sep)
#         directories_dict['name'].append(info[-1])
#         directories_dict['path'].append(root)
#         directories_dict['size'].append(get_dir_size(root))
#         directories_dict['type'].append('directory')
#         directories_dict['parent'].append(info[-2])
#         for file in files:
#             file_info = root.split(os.sep)
#             directories_dict['name'].append(file)
#             directories_dict['path'].append(root)
#             directories_dict['size'].append(os.path.getsize(f'{root}\{file}'))
#             directories_dict['type'].append('file')
#             directories_dict['parent'].append(file_info[-2])
#     save_to_json(directories_dict)
#     save_to_csv(directories_dict)
#     save_to_pickle(directories_dict)
#
#
#     # for i in range(directories_dict['name'].__len__()):
#     #     print(directories_dict['name'][i], directories_dict['path'][i], directories_dict['size'][i],
#     #           directories_dict['type'][i], directories_dict['parent'][i], sep='\t')
#
#
# get_dir_info('D:\\test')
# Задача 2. Объединение данных из нескольких JSON файлов
# Напишите скрипт, который объединяет данные из нескольких JSON файлов в
# один. Каждый файл содержит список словарей, описывающих сотрудников
# компании (имя, фамилия, возраст, должность). Итоговый JSON файл должен
# содержать объединённые списки сотрудников из всех файлов.
# Пример: У вас есть три файла employees1.json, employees2.json,
# employees3.json. Нужно объединить их в один файл all_employees.json.
# import glob
# import json
# import os
#
#
# def json_join(source_dir, output_file):
#     os.chdir(source_dir)
#     json_files = glob.glob('*.json')
#     all_in_one_list = []
#     for file in json_files:
#         with open(file, 'r') as f:
#             data = json.load(f)
#             all_in_one_list.extend(data)
#
#     with open(output_file, 'w') as f:
#         json.dump(all_in_one_list, f, indent=4)
#
#
# json_join('D:\\test', 'D:\\test\\all_in_one.json')
import csv
import json

# Задача 3. Агрегирование данных из CSV файла
# Напишите скрипт, который считывает данные из JSON файла и сохраняет их в CSV
# файл. JSON файл содержит данные о продуктах (название, цена, количество на
# складе). В CSV файле каждая строка должна соответствовать одному продукту.
# Пример: Из файла products.json нужно создать products.csv.
# def from_json_to_csv(json_file, csv_output_file):
#     with open(json_file, 'r') as f:
#         data = json.load(f)
#     with open(csv_output_file, 'w', newline='') as csv_file:
#         writer = csv.DictWriter(csv_file, fieldnames=['name', 'price', 'quantity'])
#         writer.writeheader()
#         writer.writerows(data)
#
# from_json_to_csv('D:\\test\\products.json', 'D:\\test\\from_json.csv')

# Задача 4. Агрегирование данных из CSV файла
# Напишите скрипт, который считывает данные из CSV файла, содержащего
# информацию о продажах (название продукта, количество, цена за единицу), и
# подсчитывает общую выручку для каждого продукта. Итог должен быть сохранён в
# новом CSV файле.
# def from_csv_to_csv(input_file, output_file):
#     with open(input_file, 'r') as csv_file:
#         data = list(csv.reader(csv_file, delimiter=','))
#         data[0].append('total-price')
#         for row in range(1, len(data)):
#             data[row].append(round(float(data[row][1]) * float(data[row][2]), 2))
#     with open(output_file, 'w', newline='') as csv_file:
#         csv_writer = csv.writer(csv_file)
#         csv_writer.writerows(data)
#
#
# from_csv_to_csv('D:\\test\\sales.csv', 'D:\\test\\mod_sales.csv')
# import csv
# import json
#
#
# def from_csv_to_json(input_file, output_file):
#     sort_by_author = {}
#     with open(input_file, 'r') as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             author = row['автор']
#             book = {
#                 'название': row['название'],
#                 'год издания': row['год издания']
#             }
#             if author in sort_by_author:
#                 sort_by_author[author].append(book)
#             else:
#                 sort_by_author[author] = [book]
#
#     with open(output_file, 'w') as f:
#         json.dump(sort_by_author, f, indent=4)
#
#
# from_csv_to_json('books.csv', 'sort_by_author.json')
