"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, name: str, description: str, price: float, weight: float) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight
    
    # Также можно через __repr__
    def get_full_info(self) -> str:
        return f"Информация о продукте: название - {self.name}, описание - {self.description}, цена - {self.price}, вес - {self.weight}"


if __name__ == '__main__':
    product = Product(name='Картошка', description='Мытая, молодая', price=31.4, weight=1.3)
    print(product.get_full_info())
