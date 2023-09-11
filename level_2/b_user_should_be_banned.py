"""
Нам неоюходимо проверить, находится ли фамилия пользователя в списке запрещенных.

Задания:
    1. Cоздайте класс юзера, у которого параметры: имя, фамилия, возраст.
    2. Добавьте ему метод should_be_banned, который проверяет, должен ли быть пользователь забанен.
       Пользователя стоит забанить, если его фамилия находится в SURNAMES_TO_BAN.
"""

SURNAMES_TO_BAN = ['Vaughn', 'Wilhelm', 'Santaros', 'Porter', 'Smith']


class User:
    def __init__(self, name: str, surname: str, age: int) -> None:
        self.name = name
        self.surname = surname
        self.age = age

    def should_be_banned(self) -> bool:
        banned = True if self.surname in SURNAMES_TO_BAN else False
        return banned


if __name__ == '__main__':
    user1 = User(name='Bob', surname='hghfg', age=50)
    user2 = User(name='Mark', surname='Porter', age=25)
    print(user1.should_be_banned())
    print(user2.should_be_banned())
