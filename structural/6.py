# Калькулятор стрельбы.
import datetime as dt
from typing import Dict, List, Union
from math import sin, radians, asin, degrees
# начальные условия
SHELL_VELOCITY: float = 1000  # Скорость снаряда м/с
G: float = 9.81  # Ускорение свободного падения м/c**2
history: List[Dict[str, Union[float, str]]] = []


def shoot(battery_name: str, range: float) -> None:
    """Расчитывает параметры выстрела,
    печатает их и добавляет в список выстрелов.
    battery_name - название орудия
    """
    fire_time = dt.datetime.now().strftime("%Y-%m-%d-%H.%M.%S")
    angle = get_angle(range)  # Определяем угол
    time = get_time(angle)  # Определяем полетное время
    history_append(battery_name, fire_time, angle, time)  # Добавляем в историю
    print(f'Стреляет орудие: {battery_name}\n'
          f'Время выстрела: {fire_time}\n'
          f'Угол: {angle}\n'
          f'Время полета: {time}\n'
          )


def history_append(
        battery_name: str, fire_time: str, angle: float, time: float) -> None:
    """Добавляет информацию о выстреле в список history"""
    history.append({
        'орудие': battery_name,
        'время выстрела': fire_time,
        'угол': angle,
        'время полета': time,
        })


def get_angle(distance: float) -> float:
    """Возвращает угол возвышения орудия в градусах, округленное до сотых.
    distance - расстояние до цели в метрах.
    """
    angle = degrees(
        0.5 * asin(distance * G / (SHELL_VELOCITY**2))
    )
    return round(angle, 2)


def get_time(angle: float) -> float:
    """Возвращает время полета снаряда в секундах, округленное до сотых.
    angle - угол в градусах.
    """
    time = ((2*SHELL_VELOCITY) * sin(radians(angle))) / G
    return round(time, 2)


if __name__ == "__main__":
    shoot('первая супапушга', 100000)
    shoot('фторая супапушга', 50000.5)
    shoot('первая супапушга', 1000.9)
    print(history)
