"""Модель дискретных измерений угла груза."""

from random import Random

from ...domain.parameters import MeasurementSettings
from ...domain.state import AngleMeasurement, LoadState


def measure_angle(
    load: LoadState,
    time: float,
    dt: float,
    settings: MeasurementSettings,
    rng: Random,
) -> AngleMeasurement:
    """Сформировать отсчет с шумом и временем доставки."""
    # TODO: Добавить шум к углу и вычислить время доставки по задержке.
    raise NotImplementedError("Измерительный канал еще не реализован.")
