# Калькулятор стрельбы
import datetime as dt
from typing import Dict, List, Union


class Shoot:
    def __init__(self, battery_name: str, range: float) -> None:
        self.battery_name = battery_name  # Определяем название орудия
        self.range = range  # Определяем название орудия
        # Определяем время выстрела
        self.fire_time = dt.datetime.now().strftime("%Y-%m-%d-%H.%M.%S")

    def fire(self) -> None:
        """Производит выстрел"""
        self.angle = Calculator().get_angle(self.range)  # Определяем угол
        # Определяем полетное время
        self.time = Calculator().get_time(self.angle)
        # Добавляем в историю
        History().history_append(self.battery_name,
                                 self.fire_time,
                                 self.angle,
                                 self.time)

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

    def get_angle(self, distance: float) -> float:
        """Возвращает угол возвышения орудия в градусах,
        округленное до сотых.
        distance - расстояние до цели в метрах.
        """
        ...

    def get_time(self, angle: float) -> float:
        """Возвращает время полета снаряда в секундах, округленное до сотых.
        angle - угол в градусах.
        """
        ...


class History():
    """Хранение информации о выстрелах"""
    history: List[Dict[str, Union[float, str]]] = []

    def history_append(self,
                       battery_name: str,
                       fire_time: str,
                       angle: float,
                       time: float) -> None:
        """Добавляет информацию о выстреле в список history"""
        ...


if __name__ == "__main__":
    shoot1 = Shoot('первая супапушга', 10000)
    shoot1.fire()
    print(History.history)
