class Cat:
    age: int = 0  # Свойства класса
    name: str = ''

    def show(self) -> None:  # Метод класса
        print('свойсво класса', Cat.age)
        print('свойство оъекта', self.age)
        print(self.name)


a = Cat()
print(dir(a))  # а какие атрибуты и методы есть?

a.age = 4
a.show()
