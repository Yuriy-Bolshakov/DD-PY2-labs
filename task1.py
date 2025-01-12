import doctest
class x:
    def __init__(self, views_number: int, likes_number: int):
        """
        Создание и подготовка объекта "Соцсеть"

        :param views_number: Количество просмотров
        :param likes_number: Количество лайков

        Примеры:
        >>> x = x(500, 600)  # Инициализация экземпляра класса
        >>> x.views_number
        500
        >>> x.likes_number
        600
        """
        if not isinstance(views_number, int):
            raise TypeError("Количество просмотров должно быть типа int")
        if views_number < 0:
            raise ValueError("Количество просмотров должно быть неотрицательным числом")
        self.views_number = views_number

        if not isinstance(likes_number, int):
            raise TypeError("Количество лайков должно быть типа int")
        if likes_number < 0:
            raise ValueError("Количество лайков должно быть неотрицательным числом")
        self.likes_number = likes_number

    def system_operation(self) -> bool:
        """
        Функция, которая проверяет наличие просмотров и лайков

        :return: True, если есть просмотры и лайки, иначе False

        Примеры:
        >>> x = x(500, 600)
        >>> x.system_operation()
        True
        """
        return self.views_number > 0 and self.likes_number > 0

    def detection_of_violation(self) -> bool:
        """
        Обнаружение обмана программы (накрутка)

        :return: True, если есть факт нарушения, иначе False

        Примеры:
        >>> x = x(500, 600)
        >>> x.detection_of_violation()
        False
        """
        return self.likes_number > self.views_number


class Cistern:
    def __init__(self, cistern_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Цистерна"

        :param cistern_volume: Объем цистерны
        :param occupied_volume: Объем занимаемого топлива

        Примеры:
        >>> cistern = Сistern(100, 50)  # Инициализация экземпляра класса
        >>> cistern.cistern_volume
        100
        >>> cistern.occupied_volume
        50
        """
        if not isinstance(cistern_volume, (int, float)):
            raise TypeError("Объем цистерны должен быть типа int или float")
        if cistern_volume <= 0:
            raise ValueError("Объем топливного бака должен быть положительным")
        self.cistern_volume = cistern_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Объем топлива должен быть типа int или float")
        if occupied_volume < 0:
            raise ValueError("Количество топлива должно быть неотрицательным")
        self.occupied_volume = occupied_volume

    def fuel_waste(self, spent_fuel: float) -> None:
        """
        Расход бензина из-за отработки

        :param spent_fuel: Объем отработанного бензина
        :raise ValueError: Если количество отработанного топлива превышает количество топлива в цистерне.

        Примеры:
        >>> cistern = Сistern(100, 50)
        >>> cistern.fuel_waste(20)
        >>> cistern.occupied_volume
        30
        >>> cistern.fuel_waste(50)  # Это вызовет ошибку
        Traceback (most recent call last):
            ...
        ValueError: Недостаточно топлива в цистерне
        """
        if spent_fuel > self.occupied_volume:
            raise ValueError("Недостаточно топлива в цистерне")
        self.occupied_volume -= spent_fuel

    def cistern_filling(self, fuel: float) -> None:
        """
        Заправка цистерны

        :param fuel: Количество заправляемого топлива
        :raise ValueError: Если количество заправляемого топлива превышает свободное место.

        Примеры:
        >>> cistern = Сistern(100, 50)
        >>> cistern.cistern_filling(30)  # Успешная заправка
        >>> cistern.occupied_volume
        80
        >>> cistern.cistern_filling(30)  # Это вызовет ошибку
        Traceback (most recent call last):
            ...
        ValueError: Превышен объем
        """
        if fuel + self.occupied_volume > self.cistern_volume:
            raise ValueError("Превышен объем цистерны")
        self.occupied_volume += fuel


class wallpaper:
    def __init__(self, color: str, area: float):
        """
        Создание и подготовка к работе объекта "Обои"

        :param color: Цвет
        :param area: Площадь

        Примеры:
        >>> wallpaper = Wallpaper("красный", 100)  # Инициализация экземпляра класса
        >>> wallpaper.color
        'красный'
        >>> wallpaper.area
        100
        """
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типа str")
        self.color = color

        if not isinstance(area, (int, float)):
            raise TypeError("Площадь должна быть типа int или float")
        if area <= 0:
            raise ValueError("Площадь должна быть положительным числом")
        self.area = area

    def init(self) -> str:
        """
        Функция инициализирует обои с заданным цветом

        :raise ValueError: Если строка "Цвет" - пустая.

        Примеры:
        >>> wallpaper = Wallpaper("red", 100)
        >>> wallpaper.init()
        'Инициализированы обои цвета red'
        """
        if not self.color:
            raise ValueError("Цвет не может быть пустым")
        return f"Инициализированы обои цвета {self.color}"

    def color_change(self, new_color: str) -> None:
        """
        Изменение цвета

        :param new_color: Новый цвет
        :raise ValueError: Если new_color - пустая строка

        Примеры:
        >>> wallpaper = Wallpaper("red", 100)
        >>> wallpaper.color_change("blue")
        >>> wallpaper.color
        'blue'
        >>> wallpaper.color_change("")  # Это вызовет ошибку
        Traceback (most recent call last):
            ...
        ValueError: Новый цвет не может быть пустым
        """
        if not new_color:
            raise ValueError("Новый цвет не может быть пустым")
        self.color = new_color


if __name__ == "__main__":
    doctest.testmod()  # Тестирование примеров, которые находятся в документации