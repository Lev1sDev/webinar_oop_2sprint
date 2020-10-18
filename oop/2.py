# Калькулятор стрельбы
import datetime as dt
# начальные условия
SHELL_VELOCITY: float = 1000  # Скорость снаряда м/с
G: float = 9.81  # Ускорение свободного падения м/c**2
# где-то хранить историю???


class Shoot:
    def __init__(self, battery_name):
        self.battery_name: str = battery_name # Определяем название орудия

    # Определяем время выстрела
    # Определяем угол
    # Определяем полетное время
    # Добавляем в историю

    def fire(self, battery_name):
        """Печатает параметры выстрела"""
        print(f'Стреляет орудие: {self.battery_name}\n'
              'Время выстрела: \n'
              'Угол: \n'
              'Время полета: \n'
              )


if __name__ == "__main__":
    shoot1 = Shoot('первая супапушга')
    shoot1.fire()
