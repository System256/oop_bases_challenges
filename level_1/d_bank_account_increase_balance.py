"""
У нас есть класс банковского аккаунта со свойсвами: полное имя владельца и баланс, но не релизован
метод, который увеливает баланс.

Задания:
    1. Допишите логику в метод increase_balance, который должен увеличивать баланс банковского счета на значение income.
    2. Создайте экземпляр класса банковского счета и распечатайте баланс.
    3. Увеличьте баланс счета у экземпляра класса с помощью метода increase_balance и снова распечтайте текущий баланс.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float, income: float) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance
        self.income = income

    def increase_balance(self) -> float:
        return self.balance + self.income


if __name__ == '__main__':
    client_account = BankAccount(owner_full_name='Bob', balance=50000.9, income=6000.5)
    print(client_account.balance)
    print(client_account.increase_balance())
