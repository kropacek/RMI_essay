"""Оценивание угла и угловой скорости груза."""

from dataclasses import dataclass
from typing import Sequence

from ...domain.parameters import KalmanSettings, PendulumParameters
from ...domain.state import AngleMeasurement, LoadState


@dataclass
class KalmanEstimator:
    """Линейный фильтр Калмана для плоского маятника."""

    parameters: PendulumParameters
    settings: KalmanSettings

    def reset(self, initial_estimate: LoadState, dt: float) -> None:
        """Начать новый прогон с заданной оценки и шага дискретизации."""
        # TODO: Дискретизировать модель и инициализировать историю оценок.
        raise NotImplementedError("Инициализация фильтра еще не реализована.")

    def update(
        self,
        time: float,
        previous_acceleration: float | None,
        measurements: Sequence[AngleMeasurement],
    ) -> LoadState:
        """Обновить оценку по ускорению за прошлый шаг и новым измерениям."""
        # TODO: Прогнозировать состояние и применять поправки на момент измерения.
        raise NotImplementedError("Обновление фильтра еще не реализовано.")
