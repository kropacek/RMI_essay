"""Формирование заданной траектории переноса."""

from dataclasses import dataclass

from ...domain.parameters import TransferGeometry
from ...domain.state import ReferencePoint


@dataclass(frozen=True)
class PointToPointTrajectory:
    """Перенос вдоль одной оси с нулевыми скоростями на концах."""

    geometry: TransferGeometry
    duration: float

    def sample(self, time: float) -> ReferencePoint:
        """Вернуть положение и две производные исходной команды."""
        # TODO: Задать полином пятой степени с нулевыми ускорениями на концах.
        raise NotImplementedError("Профиль переноса еще не реализован.")
