"""Исходные значения для компьютерных экспериментов."""

from math import pi

from .domain.parameters import (
    KalmanSettings,
    MeasurementSettings,
    MetricSettings,
    MotionLimits,
    PendulumParameters,
    SimulationSettings,
    TransferGeometry,
)

# Кинематика UR5e: a_i, d_i, alpha_i.
UR5E_DH = (
    (0.0, 0.1625, pi / 2),
    (-0.4250, 0.0, 0.0),
    (-0.3922, 0.0, 0.0),
    (0.0, 0.1333, pi / 2),
    (0.0, 0.0997, -pi / 2),
    (0.0, 0.0996, 0.0),
)
FLANGE_ROTATION = (
    (1.0, 0.0, 0.0),
    (0.0, -1.0, 0.0),
    (0.0, 0.0, -1.0),
)

# Перенос и пределы движения.
GEOMETRY = TransferGeometry(
    start_x=0.35,
    target_x=0.60,
    lateral_y=0.0,
    height=0.65,
    attachment_offset=(0.0, 0.0, 0.05),
)
TRANSFER_DURATION = 2.0
MOTION_LIMITS = MotionLimits(max_speed=0.3, max_acceleration=0.8)

# Маятник и начальное состояние.
PENDULUM = PendulumParameters(length=0.5, damping_ratio=0.03, gravity=9.81)
SIMULATION = SimulationSettings(
    dt=0.01,
    observation_time=5.0,
    initial_angle=0.1,
    initial_angular_velocity=0.0,
)

# Измерения и фильтр Калмана.
MEASUREMENTS = MeasurementSettings(noise_std=0.005, delay_steps=3, seed=42)
KALMAN = KalmanSettings(
    initial_variances=(0.01, 0.04),
    process_variances=(1e-6, 1e-4),
    measurement_variance=MEASUREMENTS.noise_std**2,
)

# Базовое слежение за подвесом.
TRACKING_POSITION_GAIN = 9.0
TRACKING_VELOCITY_GAIN = 6.0

# Критерии сравнения.
METRICS = MetricSettings(
    position_tolerance=0.005,
    angle_tolerance=0.02,
    residual_window=2.0,
    dwell_time=0.5,
)
