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
    return float(sum(values))


def multiply_six(data: Sequence[float]) -> float:
    """Return the product of exactly six numeric values.

    Args:
        data: A sequence containing six numeric values. The values may be
            any type that supports multiplication (int, float, Decimal, etc.).

    Returns:
        The arithmetic product of the provided values.

    Raises:
        ValueError: If ``data`` does not contain exactly six elements.
    """
    if len(data) != 6:
        raise ValueError("multiply_six requires exactly six values")

    result = 1.0
    for value in data:
        result *= value
    return result


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

    parser = argparse.ArgumentParser(
        description="Perform mathematical operations on numbers."
    )
    parser.add_argument(
        "--operation",
        choices=["sum", "multiply"],
        default="sum",
        help="Operation to perform: sum (5 numbers) or multiply (6 numbers)",
    )
    parser.add_argument(
        "numbers",
        metavar="N",
        type=float,
        nargs="+",
        help="Numeric values to process",
    )

    args = parser.parse_args(argv)

    if args.operation == "sum":
        if len(args.numbers) != 5:
            parser.error("sum operation requires exactly 5 numbers")
        result = sum_five(args.numbers)
    elif args.operation == "multiply":
        if len(args.numbers) != 6:
            parser.error("multiply operation requires exactly 6 numbers")
        result = multiply_six(args.numbers)

    print(result)


if __name__ == "__main__":  # pragma: no cover - script entry point
    main()
