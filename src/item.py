import csv
import exceptions.exceptions


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self) -> str:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return f"{self.name}: {self.price} {self.quantity}"

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = float(self.price * self.pay_rate)
        return self.price

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price} {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    @property
    def get_name(self):
        return self.name

    def name(self):
        return self.name

    def set_name(self, name):
        if len(name) < 11:
            self.name = name
        else:
            raise ValueError('Длинная наименования товаров превышает 10 символов.')

    @classmethod
    def instantiate_from_csv(cls):
        try:
            with open('../homework-6/items.csv', 'r', encoding='windows-1251') as file:
                item = csv.DictReader(file, delimiter=',')
                for i in item:
                    if any(i.get(value) is None for value in ['name', 'price', 'quantity']):
                        raise exceptions.InstantiateCSVError
                    name, price, quantity = i.get('name'), int(i.get('price')), int(i.get('quantity'))
                    cls.all.append((name, price, quantity))
        except exceptions.InstantiateCSVError as e:
            print(e)
        except FileNotFoundError:
            print('Отсутствует файл item.csv')

    @staticmethod
    def string_to_number(any_string: str) -> int:
        try:
            return int(any_string)
        except ValueError:
            return int(any_string[0: any_string.find('.')])
