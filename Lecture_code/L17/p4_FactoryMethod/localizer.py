from abc import ABC, abstractmethod


class AbstractLocalizer(ABC):

    @abstractmethod
    def localize(self, message):
        pass


class EnglishLocalizer(AbstractLocalizer):

    def localize(self, message):
        return message


class SpanishLocalizer(AbstractLocalizer):

    def __init__(self):
        self.translations = {'red': 'rojo',
                             'white': 'blanco'}

    def localize(self, message):
        return self.translations.get(message, message)


class UkrainianLocalizer(AbstractLocalizer):

    def __init__(self):
        self.translations = {'red': 'червоний',
                             'white': 'білий'}

    def localize(self, message):
        return self.translations.get(message, message)


class LocalizerFactory:

    def __init__(self):
        self.local_mapping = {'en': EnglishLocalizer,
                              'es': SpanishLocalizer,
                              'ua': UkrainianLocalizer}

    def get_localizer(self, local):
        return self.local_mapping[local]()


current_localizer = LocalizerFactory().get_localizer('es')
print(current_localizer.localize('red'))
