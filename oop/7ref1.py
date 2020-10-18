# Калькулятор стрельбы
import datetime as dt
from typing import Dict, List, Union
from math import sin, radians, asin, degrees


# Добавим пушки
class Gun:
    """Описывает пушку"""
    def __init__(self, name: str, velocity: float) -> None:
        self.name = name  # Определяем название орудия
        self.velocity = velocity  # Определяем скорость снаряда


class Action:
    def __init__(self) -> None:
        # Определяем время выстрела
        self.fire_time = dt.datetime.now().strftime("%Y-%m-%d-%H.%M.%S")

    def fire(self, gun: Gun, range: float) -> None:
        """Производит выстрел"""
        # Определяем угол
        self.angle = Calculator.get_angle(range, gun.velocity)
        # Определяем полетное время
        self.time = Calculator.get_time(self.angle, gun.velocity)
        # Добавляем в историю
        History().history_append(gun.name,
                                 self.fire_time,
                                 self.angle,
                                 self.time)

        print(f'Стреляет орудие: {gun.name}\n'
              f'Время выстрела: {self.fire_time}\n'
              f'Угол: {self.angle}\n'
              f'Время полета: {self.time}\n'
              )


class Calculator():
    """Математические расчеты для выстрела"""
    # начальные условия
    G: float = 9.81  # Ускорение свободного падения м/c**2

    @staticmethod
    def get_angle(distance: float, velocity: float) -> float:
        """Возвращает угол возвышения орудия в градусах,
        округленное до сотых.
        distance - расстояние до цели в метрах.
        """
        angle = degrees(
         0.5 * asin(distance * Calculator.G / (velocity**2))
        )
        return round(angle, 2)

    @staticmethod
    def get_time(angle: float, velocity: float) -> float:
        """Возвращает время полета снаряда в секундах, округленное до сотых.
        angle - угол в градусах.
        """
        time = (
         ((2*velocity) * sin(radians(angle))) / Calculator.G
        )
        return round(time, 2)


class History():
    """Хранение информации о выстрелах"""
    history: List[Dict[str, Union[float, str]]] = []

    def history_append(self,
                       battery_name: str,
                       fire_time: str,
                       angle: float,
                       time: float) -> None:
        """Добавляет информацию о выстреле в список history"""
        History.history.append({
            'орудие': battery_name,
            'время выстрела': fire_time,
            'угол': angle,
            'время полета': time,
            })


if __name__ == "__main__":
    gun1 = Gun('Первая пушга', 1000)
    action = Action()
    action.fire(gun1, 10000)
    action.fire(gun1, 100000)
    print(History.history)
