"""Данные, которыми обмениваются модель, фильтр и регуляторы."""

from dataclasses import dataclass


@dataclass(frozen=True)
class SupportState:
    """Положение и скорость точки подвеса вдоль оси переноса, в СИ."""

    position: float
    velocity: float


@dataclass(frozen=True)
class LoadState:
    """Угол от вертикали вниз и его производная, в рад и рад/с."""

    angle: float
    angular_velocity: float


@dataclass(frozen=True)
class PlantState:
    """Состояние подвеса и груза на одном шаге."""

    support: SupportState
    load: LoadState


@dataclass(frozen=True)
class ReferencePoint:
    """Заданные положение, скорость и ускорение вдоль оси переноса."""

    position: float
    velocity: float
    acceleration: float


@dataclass(frozen=True)
class AngleMeasurement:
    """Измеренный угол и время измерения и доставки, в секундах."""

    angle: float
    sampled_at: float
    received_at: float
