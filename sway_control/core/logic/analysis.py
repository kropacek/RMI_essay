"""Метрики переноса"""

from ...domain.parameters import MetricSettings, PendulumParameters
from ...domain.results import SimulationResult, TransferMetrics


def evaluate_transfer(
    result: SimulationResult,
    parameters: PendulumParameters,
    command_duration: float,
    settings: MetricSettings,
) -> TransferMetrics:
    """Рассчитать метрики по состоянию модели и заданию переноса."""
    # TODO: Восстановить положение груза и проверить допуски на общем интервале.
    raise NotImplementedError("Метрики переноса еще не реализованы.")
