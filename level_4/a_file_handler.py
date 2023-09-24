"""
У нас есть класс FileHandler, который может считывать файлы, но не всегда в удобном для нас виде.
Поэтому мы создали два его наследника: CSVHandler и JSONHandler

Задания:
    1. Переопределите метод read у CSVHandler и JSONHandler
    2. Метод read у JSONHandler должен возвращать словарь. Для этого используйте модуль встроенный модуль json
    3. Метод read у CSVHandler должен возвращать список словарей. Для этого используйте модуль встроенный модуль csv
    4. Создайте экземпляры каждого из трех классов.
       С помощью экземпляра FileHandler прочитайте и распечатайте содержимое файла text.txt
       С помощью экземпляра JSONHandler прочитайте и распечатайте содержимое файла recipes.json
       С помощью экземпляра CSVHandler прочитайте и распечатайте содержимое файла user_info.csv

"""
import csv
import json
from typing import Any


class FileHandler:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def read(self) -> str:
        try:
            with open(self.filename, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return f"Запрашиваемый файл {self.filename} не найден"


class JSONHandler(FileHandler):
    def read(self) -> dict[str]:
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return data                      
        except FileNotFoundError:
            return f"Запрашиваемый файл {self.filename} не найден"
        except json.JSONDecodeError:
            return f"Указанный файл {self.filename} не json"
            
        
class CSVHandler(FileHandler):
    def read(self) -> list[str]:
        try:
            with open(self.filename, 'r') as file:
                data = csv.DictReader(file)
                list_data = [row for row in data]
                return list_data
        except FileNotFoundError:
            return f"Запрашиваемый файл {self.filename} не найден"


if __name__ == '__main__':
    print('-' * 60)

    file_txt = FileHandler(filename='level_4\\data\\text.txt')
    print(file_txt.read())

    print('-' * 60)

    file_json = JSONHandler(filename='level_4\\data\\recipes.json')
    print(file_json.read())

    print('-' * 60)

    file_csv = CSVHandler(filename='level_4\\data\\user_info.csv')
    print(file_csv.read())

    print('-' * 60)