"""Схема исходной конфигурации переноса."""

from pathlib import Path

from ....domain.parameters import PendulumParameters, TransferGeometry
from ....domain.state import LoadState
from ..kinematics import Matrix


def plot_initial_setup(
    geometry: TransferGeometry,
    parameters: PendulumParameters,
    initial_load: LoadState,
    output_path: Path,
    *,
    frames: tuple[Matrix, ...] | None = None,
) -> None:
    """Сохранить схему подвеса, начального положения груза и направления переноса."""
    # TODO: Показать начальный угол и длину подвеса. При наличии frames добавить звенья.
    raise NotImplementedError("Визуализация начальной конфигурации еще не реализована.")
