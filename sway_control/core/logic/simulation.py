"""Связь модели, измерений и управления на дискретной сетке."""

from ..interfaces import Controller, Plant, ReferenceTrajectory
from ...domain.parameters import MeasurementSettings, SimulationSettings
from ...domain.results import SimulationResult
from ...domain.state import LoadState
from .estimator import KalmanEstimator


def simulate(
    plant: Plant,
    trajectory: ReferenceTrajectory,
    controller: Controller,
    settings: SimulationSettings,
    *,
    measurements: MeasurementSettings | None = None,
    estimator: KalmanEstimator | None = None,
    initial_estimate: LoadState | None = None,
) -> SimulationResult:
    """Провести перенос с точным состоянием или оценками фильтра."""
    # TODO: Обрабатывать доставленные отсчеты перед расчетом команды на новый шаг.
    raise NotImplementedError("Цикл моделирования еще не реализован.")


def record_free_decay(
    plant: Plant,
    settings: SimulationSettings,
    measurements: MeasurementSettings,
    duration: float,
) -> SimulationResult:
    """Записать затухание при неподвижной точке подвеса."""
    # TODO: Использовать нулевое ускорение и тот же измерительный канал.
    raise NotImplementedError("Запись свободного затухания еще не реализована.")
