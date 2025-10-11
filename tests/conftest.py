"""Shared pytest fixtures and configuration for all tests."""

from typing import List, Sequence

import pytest


@pytest.fixture
def valid_five_numbers() -> List[float]:
    """Provide a list of five valid numbers for sum_five testing."""
    return [1.0, 2.0, 3.0, 4.0, 5.0]


@pytest.fixture
def valid_six_numbers() -> List[float]:
    """Provide a list of six valid numbers for multiply_six testing."""
    return [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]


@pytest.fixture
def mixed_sign_six_numbers() -> List[float]:
    """Provide a list of six numbers with mixed signs."""
    return [2.0, -3.0, 4.0, -5.0, 6.0, 7.0]


@pytest.fixture
def six_numbers_with_zero() -> List[float]:
    """Provide a list of six numbers including zero."""
    return [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]


@pytest.fixture
def large_six_numbers() -> List[float]:
    """Provide a list of six large numbers for testing edge cases."""
    return [1e6, 2e6, 3e6, 4e6, 5e6, 6e6]


@pytest.fixture
def small_six_numbers() -> List[float]:
    """Provide a list of six small numbers for testing precision."""
    return [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]


@pytest.fixture
def invalid_four_numbers() -> List[float]:
    """Provide an invalid list with only four numbers."""
    return [1.0, 2.0, 3.0, 4.0]


@pytest.fixture
def invalid_seven_numbers() -> List[float]:
    """Provide an invalid list with seven numbers."""
    return [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]


@pytest.fixture
def string_number_list() -> List[str]:
    """Provide a list of string representations of numbers."""
    return ["1.5", "2.5", "3.5", "4.5", "5.5", "6.5"]


@pytest.fixture
def invalid_string_list() -> List[str]:
    """Provide a list with invalid string representations."""
    return ["1.5", "not_a_number", "3.5", "4.5", "5.5"]
