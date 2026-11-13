"""Записи симуляции и рассчитанные показатели."""

from dataclasses import dataclass

from .state import AngleMeasurement, LoadState, PlantState, ReferencePoint


@dataclass(frozen=True)
class SimulationSample:
    """Состояние и команды на шаге. Ускорения относятся к следующему интервалу."""

    time: float
    state: PlantState
    reference: ReferencePoint
    estimate: LoadState | None
    command: float | None
    applied_acceleration: float | None


@dataclass(frozen=True)
class SimulationResult:
    """История переноса и запись измерений с временными метками."""

    samples: tuple[SimulationSample, ...]
    measurements: tuple[AngleMeasurement, ...]


@dataclass(frozen=True)
class TransferMetrics:
    """Остаточный угол, конечная ошибка груза и время до допуска."""

    residual_angle: float
    final_position_error: float
    time_to_tolerance: float | None
