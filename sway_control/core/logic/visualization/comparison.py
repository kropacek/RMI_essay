"""Представление результатов сравнения регуляторов."""

from pathlib import Path
from typing import Mapping

from ....domain.results import SimulationResult, TransferMetrics


def export_comparison(
    results: Mapping[str, SimulationResult],
    metrics: Mapping[str, TransferMetrics],
    output_dir: Path,
) -> None:
    """Сохранить графики переноса и сводную таблицу."""
    # TODO: Показать углы и положение подвеса на общей шкале времени.
    raise NotImplementedError("Экспорт сравнения еще не реализован.")
