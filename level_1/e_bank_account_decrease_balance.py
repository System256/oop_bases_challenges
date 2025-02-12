"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float) -> float:
        self.balance += amount
        return self.balance
    
    def decrease_balance(self, amount: float) -> float:
        self.balance -= amount
        if self.balance < 0:
            raise ValueError('Баланс не может быть отрицательным.')
        return self.balance


if __name__ == '__main__':
    client_account = BankAccount(owner_full_name='Alex', balance=10586.5)
    print(client_account.decrease_balance(amount=8000))
    print(client_account.balance)
    print(client_account.decrease_balance(amount=8000))
