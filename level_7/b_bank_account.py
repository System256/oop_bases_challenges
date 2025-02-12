"""
Банк позволяет уходить в минус по счету, чтобы клиенты не оказывались в без денег в самый неподходящий момент

Задания:
    1. Напишите логику метода decrease_balance таким образом, чтобы можно было уменьшать баланс, но чтобы он не становился
       меньше чем значение в атрибуте класса min_balance. Если он будет меньше - вызывайте исключение ValueError
    2. Создайте экземпляр класса BankAccount, вызовите у него метод decrease_balance и убедитесь, что баланс уменьшается
       и если он уменьшается больше чем можно, то вызывается исключение
"""


class BankAccount:
    min_balance = -100

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    def decrease_balance(self, amount: float) -> ValueError:
        self.balance -= amount
        if self.balance < self.min_balance:
            raise ValueError(f'Баланс не может быть менее {self.min_balance}')


if __name__ == '__main__':
    bank_account = BankAccount(owner='Eddie', balance=200.5)
    bank_account.decrease_balance(amount=100)
    print(bank_account.balance)
    bank_account.decrease_balance(amount=400)
