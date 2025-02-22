class Dog(Animal):
    """
    Дочерний класс для собак.
    Атрибуты:
        name (str): Имя собаки.
        age (int): Возраст собаки.
        breed (str): Порода собаки.
    """
    def __init__(self, name: str, age: int, breed: str):
        """
        Конструктор дочернего класса Dog.
        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age, species="Dog")
        self.breed = breed
    def make_sound(self) -> str:
        """
        Перегрузка метода make_sound для собаки.
        :return: Строка с описанием звука, издаваемого собакой.
        """
        return "Woof!"
    def fetch(self, item: str) -> str:
        """
        Метод, который описывает, как собака приносит предмет.
        :param item: Предмет, который нужно принести.
        :return: Строка с описанием действия.
        """
        return f"{self.name} is fetching the {item}."
    def __str__(self) -> str:
        """
        Перегрузка магического метода для строкового представления объекта.
        :return: Строка с описанием собаки.
        """
        return f"{self.name} is a {self.age}-year-old {self.breed} dog."
    def __repr__(self) -> str:
        """
        Перегрузка магического метода для представления объекта в виде строки, которая может быть использована для воссоздания объекта.
        :return: Строка, которая может быть использована для создания объекта.
        """
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"
    class Cat(Animal):
        """
        Дочерний класс для кошек.
        Атрибуты:
            name (str): Имя кошки.
            age (int): Возраст кошки.
            color (str): Цвет кошки.
        """
        def __init__(self, name: str, age: int, color: str):
            """
            Конструктор дочернего класса Cat.
            :param name: Имя кошки.
            :param age: Возраст кошки.
            :param color: Цвет кошки.
            """
            super().__init__(name, age, species="Cat")
            self.color = color
        def make_sound(self) -> str:
            """
            Перегрузка метода make_sound для кошки.
            :return: Строка с описанием звука, издаваемого кошкой.
            """
            return "Meow!"
        def scratch(self) -> str:
            """
            Метод, который описывает, как кошка царапается.
            :return: Строка с описанием действия.
            """
            return f"{self.name} is scratching."
        def __str__(self) -> str:
            """
            Перегрузка магического метода для строкового представления объекта.
            :return: Строка с описанием кошки.
            """
            return f"{self.name} is a {self.age}-year-old {self.color} cat."
        def __repr__(self) -> str:
            """
            Перегрузка магического метода для представления объекта в виде строки, которая может быть использована для воссоздания объекта.
            :return: Строка, которая может быть использована для создания объекта.
            """
            return f"Cat(name={self.name}, age={self.age}, color={self.color})"