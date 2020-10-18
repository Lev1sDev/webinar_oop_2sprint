# Калькулятор стрельбы.
import datetime as dt
from typing import Dict, List, Union
# начальные условия
SHELL_VELOCITY: float = 1000  # Скорость снаряда м/с
G: float = 9.81  # Ускорение свободного падения м/c**2
history: List[Dict[str, Union[float, str]]] = []


def shoot(battery_name: str) -> None:
    """Расчитывает параметры выстрела,
    печатает их и добавляет в список выстрелов.
    battery_name - название орудия
    """
    fire_time = dt.datetime.now().strftime("%Y-%m-%d-%H.%M.%S")
    angle = get_angle()  # Определяем угол
    time = get_time()    # Определяем полетное время
    history_append()     # Добавляем в историю
    print(f'Стреляет орудие: {battery_name}\n'
          f'Время выстрела: {fire_time}\n'
          f'Угол: {angle}\n'
          f'Время полета: {time}\n'
          )


def history_append():
    """Добавляет информацию о выстреле в список history"""
    ...


def get_angle():
    """Возвращает угол возвышения орудия в градусах, округленное до сотых."""
    ...


def get_time():
    """Возвращает время полета снаряда в секундах, округленное до сотых."""
    ...


if __name__ == "__main__":
    shoot('первая супапушга')
    print(history)
