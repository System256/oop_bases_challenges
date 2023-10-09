"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""


class Product:
    def __init__(self, title: str, price: float) -> None:
        self.title = title
        self.price = price

    def get_info(self) -> str:
        return f'Product {self.title} with price {self.price}'
    

class PrintLoggerMixin():
    def log(self, message: str) -> str:
        print(f'[LOG]: {message}')


class PremiumProduct(PrintLoggerMixin, Product):
    def increase_price(self) -> None:
        self.log('Logging def increase_price')
        self.price *= 1.2

    def get_info(self) -> str:
        self.log('Logging def get_info')
        base_info = super().get_info()
        return f'{base_info} (Premium)'


class DiscountedProduct(PrintLoggerMixin, Product):
    def increase_price(self) -> None:
        self.log('Logging def increase_price')
        self.price /= 1.2

    def get_info(self) -> str:
        self.log('Logging def get_info')
        base_info = super().get_info()
        return f'{base_info} (Discounted)'
    

if __name__ == '__main__':
    print('-' * 60)

    premium_product = PremiumProduct(title='Banana', price=150)
    premium_product.increase_price()
    print(premium_product.get_info())

    print('-' * 60)

    discounted_product = DiscountedProduct(title='Kiwi', price=50)
    discounted_product.increase_price()
    print(discounted_product.get_info())

    print('-' * 60)