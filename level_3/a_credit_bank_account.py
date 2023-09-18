"""
У нас есть класс кредитного банковского аккаунта со свойсвами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""
from decimal import Decimal


class BankAccount:
    def __init__(self, owner_full_name: str, balance: Decimal = 0) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: Decimal) -> None:
        self.balance += amount

    def decrease_balance(self, amount: Decimal) -> Decimal:
        self.balance -= amount
        if self.balance < 0:
            raise ValueError('Баланс не может быть отрицательным.')
        return self.balance
    

class CreditAccount(BankAccount):
    def __init__(self, owner_full_name: str, balance: Decimal = 0) -> None:
        super().__init__(owner_full_name, balance)

    def is_eligible_for_credit(self) -> bool:
        return self.balance > 1000


if __name__ == '__main__':
    print('-' * 60)

    client_account = BankAccount(owner_full_name='Bob', balance=Decimal(6000))
    client_account.increase_balance(amount=Decimal(5200))
    print(client_account.balance)
    client_account.decrease_balance(amount=Decimal(100))
    print(client_account.balance)

    print('-' * 60)

    client_credit_account = CreditAccount(owner_full_name='Alex', balance=Decimal(46000))
    print(client_credit_account.is_eligible_for_credit())
    client_credit_account.decrease_balance(amount=Decimal(3000))
    print(client_credit_account.balance)
    client_credit_account.increase_balance(amount=Decimal(6000))
    print(client_credit_account.balance)

    print('-' * 60)