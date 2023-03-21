"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_item_init(item):
    assert item.name == 'Смартфон'
    assert item.price == 10000
    assert item.quantity == 20


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 'Смартфон: 10000 20'


def test_str_to_num():
    assert Item.string_to_number('9.2') == 9


def test_str(item):
    assert str(item) == "Смартфон"


def test_repr(item):
    assert repr(item) == "Item('Смартфон', 10000 20)"






