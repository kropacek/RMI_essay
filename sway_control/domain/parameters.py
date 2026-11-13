"""Параметры модели и эксперимента."""

from dataclasses import dataclass


@dataclass(frozen=True)
class TransferGeometry:
    """Координаты в базе и смещение крепления в системе фланца, в метрах."""

    start_x: float
    target_x: float
    lateral_y: float
    height: float
    attachment_offset: tuple[float, float, float]


@dataclass(frozen=True)
class SimulationSettings:
    """Шаг расчета, время наблюдения после переноса и начальный угол."""

    dt: float
    observation_time: float
    initial_angle: float
    initial_angular_velocity: float


@dataclass(frozen=True)
class MotionLimits:
    """Пределы модуля скорости и ускорения подвеса, в СИ."""

    max_speed: float
    max_acceleration: float


@dataclass(frozen=True)
class PendulumParameters:
    """Длина в метрах, относительное демпфирование и ускорение тяжести."""

    length: float
    damping_ratio: float
    gravity: float


@dataclass(frozen=True)
class MeasurementSettings:
    """Стандартное отклонение шума в радианах и задержка в шагах."""

    noise_std: float
    delay_steps: int
    seed: int


@dataclass(frozen=True)
class KalmanSettings:
    """Диагонали ковариаций начальной ошибки и шума процесса за шаг."""

    initial_variances: tuple[float, float]
    process_variances: tuple[float, float]
    measurement_variance: float


@dataclass(frozen=True)
class MetricSettings:
    """Допуски в метрах и радианах, интервалы в секундах."""

    position_tolerance: float
    angle_tolerance: float
    residual_window: float
    dwell_time: float
