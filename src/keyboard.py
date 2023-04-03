from src.item import Item


class MixLanguages:

    def __init__(self, language='EN'):
        self._language = language

    def change_lang(self):
        if self.language == 'EN':
            self._language = 'RU'
            return self
        else:
            self._language = 'EN'
            return self

    @property
    def language(self):
        return self._language


class KeyBoard(Item, MixLanguages):
    def __str__(self):
        return super().__str__()

