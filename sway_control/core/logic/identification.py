"""Оценка параметров маятника по записи свободных колебаний."""

from typing import Sequence

from ...domain.parameters import PendulumParameters
from ...domain.state import AngleMeasurement


def estimate_parameters(
    samples: Sequence[AngleMeasurement], gravity: float
) -> PendulumParameters:
    """Оценить эффективную длину и относительное демпфирование."""
    # TODO: Найти одноименные пики и оценить период и логарифмический декремент.
    raise NotImplementedError("Идентификация еще не реализована.")
