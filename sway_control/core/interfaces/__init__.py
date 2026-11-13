"""Интерфейсы компонентов, которые можно заменить в симуляции."""

from typing import Protocol

from ...domain.state import LoadState, PlantState, ReferencePoint, SupportState


class ReferenceTrajectory(Protocol):
    """Траектория, общая для всех сравниваемых регуляторов."""

    @property
    def duration(self) -> float:
        """Вернуть длительность команды в секундах."""
        ...

    def sample(self, time: float) -> ReferencePoint:
        """Вернуть задание в момент time, после конца удерживать цель."""
        ...


class Controller(Protocol):
    """Взаимозаменяемый регулятор для одной траектории переноса."""

    def command(
        self, reference: ReferencePoint, support: SupportState, load: LoadState
    ) -> float:
        """Вернуть требуемое ускорение точки подвеса, в м/с²."""
        ...


class Plant(Protocol):
    """Модель переноса с одним входом ускорения."""

    def step(
        self, state: PlantState, command: float, dt: float
    ) -> tuple[PlantState, float]:
        """Вернуть новое состояние и фактическое ускорение за шаг."""
        ...
