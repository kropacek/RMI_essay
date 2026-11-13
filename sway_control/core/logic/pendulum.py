"""Динамика плоского маятника и ограниченного движения подвеса."""

from dataclasses import dataclass

from ...domain.parameters import MotionLimits, PendulumParameters
from ...domain.state import LoadState, PlantState


def angular_acceleration(
    load: LoadState, support_acceleration: float, parameters: PendulumParameters
) -> float:
    """Вычислить угловое ускорение по нелинейному уравнению маятника."""
    # TODO: Учесть тяжесть, вязкое сопротивление и движение точки подвеса.
    raise NotImplementedError("Уравнение маятника еще не реализовано.")


@dataclass(frozen=True)
class PlanarPlant:
    """Модель груза и идеализированного исполнительного канала."""

    parameters: PendulumParameters
    limits: MotionLimits

    def step(
        self, state: PlantState, command: float, dt: float
    ) -> tuple[PlantState, float]:
        """Вернуть новое состояние и ускорение, приложенное за шаг."""
        # TODO: Ограничить команду по скорости и ускорению, затем интегрировать.
        raise NotImplementedError("Шаг динамической модели еще не реализован.")
