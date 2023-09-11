""""
У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""


class User:
    def __init__(self, username: str, name: str = None, user_id: int = None) -> None:
        self.username = username
        self.name = name
        self.user_id = user_id

    def make_username_capitalized(self) -> str:
        return self.username.capitalize()

    def generate_short_user_description(self) -> str:
        return f'User with id {self.user_id} has {self.make_username_capitalized()} username and {self.name} name'
    

if __name__ == '__main__':
    user1 = User(username='roman555', name='roman', user_id=1)
    print(user1.generate_short_user_description())