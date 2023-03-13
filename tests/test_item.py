"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item():
    assert Item.all == []
    assert Item.pay_rate == 1.0


