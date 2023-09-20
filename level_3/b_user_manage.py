"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class UserManager:
    def __init__(self) -> None:
        self.usernames = []

    def add_user(self, username: str) -> None:
        self.usernames.append(username)
        print(f'Пользователь {username} успешно добавлен.')

    def get_users(self) -> list[str]:
        return self.usernames


class AdminManager(UserManager):
    def __init___(self, username: str) -> None:
        super().__init__(username)

    def ban_username(self, username: str) -> None:
        if username in super().get_users():
            super().get_users().remove(username)
            print(f'Пользователь {username} успешно заблокрован.')
        else:
            print(f'Пользователя {username} не существует.')


class SuperAdminManager(AdminManager):
    def ban_all_users(self) -> None:
        self.usernames.clear()
        print(f'Все пользователи успешно заблокрованы.')


if __name__ == '__main__':
    print('-' * 60)

    user_manager = UserManager()
    user_manager.add_user(username='Bob')
    print(user_manager.get_users())

    print('-' * 60)

    admin_manager = AdminManager()
    admin_manager.add_user(username='Ivan')
    admin_manager.add_user(username='Alex')
    print(admin_manager.get_users())
    admin_manager.ban_username(username='Ivan')
    print(admin_manager.get_users())
    admin_manager.ban_username(username='Igor')

    print('-' * 60)

    super_admin_manager = SuperAdminManager()
    super_admin_manager.add_user(username='Anton')
    super_admin_manager.add_user(username='Anna')
    super_admin_manager.add_user(username='Alisa')
    print(super_admin_manager.get_users())
    super_admin_manager.ban_username(username='Anna')
    print(super_admin_manager.get_users())
    super_admin_manager.ban_username(username='Roman')
    super_admin_manager.ban_all_users()
    print(super_admin_manager.get_users())
    
    print('-' * 60)