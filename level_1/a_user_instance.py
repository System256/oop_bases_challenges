"""
Задания:
    1. Создайте экземпляр класса юзера, наполнив любыми данными.
    2. Распечатайте информацию о нем в таком виде: Информация о пользователе: имя, юзернэйм, возраст, телефон.
"""


class User:
    def __init__(self, name: str, username: str, age: int, phone: str):
        self.name = name
        self.username = username
        self.age = age
        self.phone = phone


if __name__ == '__main__':
    client = User(name='Ann', username='An777', age=26, phone='+79885022266')
    print(f"Информация о пользователе: имя - {client.name}, юзернэйм - {client.username}, возраст - {client.age}, телефон - {client.phone}")

