class Cat:
    age: int = 0  # Свойства класса
    name: str = ''

    def show(self) -> None:  # Метод класса
        print(self.age)
        print(self.name)


# Создадим котейку/ экземпларя класса. или объект класса
# А какой тип?
a = Cat()
print(type(a))
a.name = 'Кузя'
a.age = 4
a.age +=1
a.show()


b = Cat()
b.name = 'Васька'
b.age = 1
# Добавим котейке еще одну ногу. Фу такими быть
b.show()
b.legs = 50
print(b.legs)
