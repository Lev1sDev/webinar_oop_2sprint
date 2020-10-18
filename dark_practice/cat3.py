# Проблема. Кошка с нулевым возрастом. Конструктор

class Cat:
    age: int = 0  # Свойства класса
    name: str = ''
    def show(self):  # Метод класса
        print(self.age)
        print(self.name)

a = Cat()
a.name = 'Васька'
a.age = 4

# А хочется что бы был обязателное имя и возраст.
# Для этих целей есть конструктор/ атрибуты становятся обязательными
# Явное лучше, чем неявное

class Cat:
    LEGS: int = 4
    def __init__(self, name: str, age: int) -> None:
        # Задача инит - сконструировать объект.
        self.name = name  # Свойство объекта
        self.age = age

    def show(self) -> None:  # Метод класса
        print(self.LEGS)
        print(Cat.LEGS)
        print(self.age)
        print(self.name)


a = Cat('Кузя', 10)
