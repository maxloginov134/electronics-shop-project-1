import pytest
from src.keyboard import MixLanguages


@pytest.fixture
def keyboard():
    return MixLanguages("HyperX Alloy Origins 60")


def test_init(keyboard):
    assert keyboard.language == 'HyperX Alloy Origins 60'


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert keyboard.language == 'EN'
    keyboard.change_lang()
    assert keyboard.language == 'RU'
