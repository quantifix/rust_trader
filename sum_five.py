"""Simple utility to sum five numbers.

This module provides a :func:`sum_five` helper that enforces the
requirement of summing exactly five numeric values.  A small command line
interface is also supplied so the script can be executed directly.
"""
from __future__ import annotations

from typing import Iterable, Sequence


def sum_five(values: Sequence[float]) -> float:
    """Return the sum of exactly five numeric values.

    Args:
        values: A sequence containing five numeric values.  The values may be
            any type that supports addition (int, float, Decimal, etc.).

    Returns:
        The arithmetic sum of the provided values.

    Raises:
        ValueError: If ``values`` does not contain exactly five elements.
    """
    if len(values) != 5:
        raise ValueError("sum_five requires exactly five values")
    return sum(values)


def parse_numbers(raw_values: Iterable[str]) -> list[float]:
    """Convert an iterable of strings to floating point numbers."""
    numbers: list[float] = []
    for item in raw_values:
        try:
            numbers.append(float(item))
        except ValueError as exc:  # pragma: no cover - defensive branch
            raise ValueError(f"Could not parse '{item}' as a number") from exc
    return numbers


def main(argv: Sequence[str] | None = None) -> None:
    """Entry point for the command line interface."""
    import argparse

    parser = argparse.ArgumentParser(description="Sum exactly five numbers.")
    parser.add_argument(
        "numbers",
        metavar="N",
        type=float,
        nargs=5,
        help="Five numeric values to sum",
    )

    args = parser.parse_args(argv)
    total = sum_five(args.numbers)
    print(total)


if __name__ == "__main__":  # pragma: no cover - script entry point
    main()
