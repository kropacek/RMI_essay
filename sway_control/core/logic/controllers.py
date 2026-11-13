"""Законы управления ускорением точки подвеса."""

from dataclasses import dataclass

from ...domain.parameters import PendulumParameters
from ...domain.state import LoadState, ReferencePoint, SupportState


@dataclass(frozen=True)
class TrackingController:
    """Базовое слежение за траекторией точки подвеса."""

    position_gain: float
    velocity_gain: float

    def command(
        self, reference: ReferencePoint, support: SupportState, load: LoadState
    ) -> float:
        """Рассчитать ускорение по ошибкам положения и скорости подвеса."""
        # TODO: Использовать знак ошибки «заданное минус текущее».
        raise NotImplementedError("Базовый регулятор еще не реализован.")


@dataclass(frozen=True)
class PDController:
    """Дополнить базовое слежение угловой обратной связью."""

    tracking: TrackingController
    angle_gain: float
    angular_velocity_gain: float

    def command(
        self, reference: ReferencePoint, support: SupportState, load: LoadState
    ) -> float:
        """Рассчитать ускорение с поправкой по углу и угловой скорости."""
        # TODO: Добавить угловую поправку к команде базового регулятора.
        raise NotImplementedError("PD-регулятор еще не реализован.")


@dataclass(frozen=True)
class LQRController:
    """Совместное управление ошибками подвеса и состоянием груза."""

    state_gain: tuple[float, float, float, float]

    @classmethod
    def design(
        cls,
        parameters: PendulumParameters,
        state_weights: tuple[float, float, float, float],
        input_weight: float,
    ) -> "LQRController":
        """Рассчитать усиление по параметрам маятника и весам критерия."""
        # TODO: Собрать матрицы из раздела 2.5 и решить уравнение Риккати.
        raise NotImplementedError("Расчет усиления LQR еще не реализован.")

    def command(
        self, reference: ReferencePoint, support: SupportState, load: LoadState
    ) -> float:
        """Рассчитать ускорение по заданию и усилению LQR."""
        # TODO: Вычислить поправку по ошибкам подвеса, углу и угловой скорости.
        raise NotImplementedError("Команда LQR еще не реализована.")
