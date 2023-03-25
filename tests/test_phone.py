import pytest
from src.phone import Phone


def test_phone_init(phone):
    assert phone.name == "iPhone super van plus"
    assert phone.price == 10000
    assert phone.quantity == 20
    assert phone.number_of_sim == 2


def test_radd_classes(phone, item):
    assert item + phone == 40


def test_add_classes(phone):
    test_phone_2 = Phone("iPhone", 200000, 5, 2)
    assert phone + test_phone_2 == 25


def test_phone_repr(phone):
    assert repr(phone) == "Phone('iPhone super van plus', 10000, 20, 2)"


def test_failed_add_classes(phone):
    with pytest.raises(TypeError):
        phone + 12
