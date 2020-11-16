import json
from keyword import iskeyword


class ColorizeMixin:
    """
    Change color Advert().__repr__
    """

    repr_color_code = 33

    def __str__(self):
        return f"\033[0;{self.repr_color_code};47m{repr(self)} "


class Advert(ColorizeMixin):
    """
    Create class dynamically, display class attributes through a dot
    """

    repr_color_code = 33

    def __init__(self, json_dict: dict):

        for key, value in json_dict.items():
            if iskeyword(key):
                key += '_'
            if isinstance(value, dict):
                setattr(self, key, Advert(value))
            else:
                setattr(self, key, value)

            try:
                if self.price < 0:
                    raise ValueError("must be >= 0")
            except AttributeError:
                self.price = 0

    def __repr__(self):
        """
        Display the title and price of the ad
        """
        return f'{getattr(self, "title")} | {getattr(self, "price")} ₽'


if __name__ == "__main__":
    lesson_str = """{
        "title": "iPhone X",
        "class": "corgi",
        "break": 23,
        "price": 100,
        "location": {
            "address": "город Самара, улица Мориса Тореза, 50",
            "metro_stations": ["Спортивная", "Гагаринская"]
        }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    # Вывод через точку
    print(lesson_ad.break_)
    # Проверка цены
    lesson_str = '{"title": "python", "price": -999}'
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.price)
    # Проверка на изменения цвета через Миксин
    iphone_ad = Advert(lesson)
    print(iphone_ad)
