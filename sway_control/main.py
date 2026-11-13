"""Точка входа для запуска компьютерных экспериментов."""

import argparse
from pathlib import Path

from .experiments.comparison import run_comparison


def main() -> None:
    """Выбрать эксперимент и передать ему путь для результатов."""
    experiments = {"comparison": run_comparison}
    parser = argparse.ArgumentParser(description="Эксперименты с подвешенным грузом.")
    parser.add_argument("experiment", choices=experiments)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs"))
    args = parser.parse_args()

    try:
        experiments[args.experiment](args.output_dir)
    except NotImplementedError as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
