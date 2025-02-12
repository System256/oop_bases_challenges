"""
У нас есть класс формы и метод для валидации в нем. Мы хотим создать форму для авторизации, где нам важно чтобы юзернэйм
существовал в базе данных

Задания:
    1. Напишите логику метода valid_form в классе AuthorizationFormMixin таким образом, чтобы там была проверка и из
       класса Form и проверка на то что юзернэйм есть в списке USERNAMES_IN_DB. Нужно использовать super() в этом методе
    2. Создайте класс AuthorizationForm, который будет наследником и от Form и от AuthorizationFormMixin
    3. Создайте экземпляр класса AuthorizationForm и вызовите у него метод valid_form. Должны отрабатывать обе проверки:
       и на длину пароля и на наличия юзернэйма в базе
"""
USERNAMES_IN_DB = ['Alice_2023', 'BobTheBuilder', 'CrazyCoder', 'DataDiva', 'EpicGamer', 'JavaJunkie']


class Form:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def valid_form(self) -> bool:
        return len(self.password) > 8


class AuthorizationFormMixin(Form):
    def valid_form(self) -> bool:
        return super().valid_form() and self.username in USERNAMES_IN_DB


class AuthorizationForm(AuthorizationFormMixin, Form):
    pass


if __name__ == '__main__':
    authorization_form_1 = AuthorizationForm(username='BobTheBuilder', password='ghgfhfgh4fg6564')
    print(authorization_form_1.valid_form())

    authorization_form_2 = AuthorizationForm(username='DataDiva', password='ghgfhfg')
    print(authorization_form_2.valid_form())

    authorization_form_3 = AuthorizationForm(username='Bob', password='ghgfhfgh4fg6564')
    print(authorization_form_3.valid_form())
