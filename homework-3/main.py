from src.item import Item

if __name__ == '__main__':
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000 20)"
    assert str(item) == "Смартфон"
