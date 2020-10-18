# Калькулятор стрельбы
import datetime as dt
from typing import Dict, List, Union


class Shoot:
    def __init__(self, battery_name: str) -> None:
        self.battery_name = battery_name  # Определяем название орудия
        # Определяем время выстрела
        self.fire_time = dt.datetime.now() .strftime("%Y-%m-%d-%H.%M.%S")

    def fire(self) -> None:
        """Производит выстрел"""
        calc = Calculator()
        self.angle = calc.get_angle()  # Определяем угол
        self.time = Calculator().get_time()    # Определяем полетное время
        History().history_append()             # Добавляем в историю

        print(f'Стреляет орудие: {self.battery_name}\n'
              f'Время выстрела: {self.fire_time}\n'
              f'Угол: {self.angle}\n'
              f'Время полета: {self.time}\n'
              )


class Calculator():
    """Математические расчеты для выстрела"""
    # начальные условия
    SHELL_VELOCITY: float = 1000  # Скорость снаряда м/с
    G: float = 9.81  # Ускорение свободного падения м/c**2

    def get_angle(self):
        """Возвращает угол возвышения орудия в градусах,
        округленное до сотых.
        """
        ...

    def get_time(self):
        """Возвращает время полета снаряда в секундах, округленное до сотых."""
        ...


class History():
    """Хранение информации о выстрелах"""
    history: List[Dict[str, Union[float, str]]] = []

    def history_append(self):
        """Добавляет информацию о выстреле в список history"""
        ...


if __name__ == "__main__":
    shoot1 = Shoot('первая супапушга')
    shoot1.fire()
    print(History().history)
