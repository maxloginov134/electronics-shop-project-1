import csv


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
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self) -> str:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return f"{self.__name}: {self.price} RUB\nВ наличии: {self.quantity} шт."

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = float(self.price * self.pay_rate)
        return self.price

    @property
    def get_name(self):
        return self.__name

    def set_name(self, value):
        if self.__name > value:
            return f"Наименование товара должно содержать {value}"
        return self.__name

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r', encoding='windows-1251') as file:
            data = csv.reader(file)
            for row in data:
                cls.all.append(row)

    @staticmethod
    def string_to_number(any_string: str) -> int:
        try:
            return int(any_string)
        except ValueError:
            return int(any_string[0: any_string.find('.')])
