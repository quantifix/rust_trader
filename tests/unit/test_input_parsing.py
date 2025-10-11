"""Unit tests for input parsing functionality."""

import os
import sys
from typing import List

import pytest

# Add the parent directory to the path to import sum_five module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from sum_five import parse_numbers


class TestParseNumbers:
    """Test cases for the parse_numbers function."""

    def test_parse_numbers_with_valid_string_numbers_returns_float_list(
        self, string_number_list
    ):
        """Test parse_numbers converts valid string numbers to floats."""
        result = parse_numbers(string_number_list)
        expected = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
        assert result == expected
        assert all(isinstance(x, float) for x in result)

    def test_parse_numbers_with_integer_strings_returns_float_list(self):
        """Test parse_numbers converts integer strings to floats."""
        int_strings = ["1", "2", "3", "4", "5"]
        result = parse_numbers(int_strings)
        expected = [1.0, 2.0, 3.0, 4.0, 5.0]
        assert result == expected

    def test_parse_numbers_with_negative_strings_returns_correct_floats(self):
        """Test parse_numbers handles negative number strings."""
        negative_strings = ["-1.5", "-2.0", "3.5", "-4.0", "5.5"]
        result = parse_numbers(negative_strings)
        expected = [-1.5, -2.0, 3.5, -4.0, 5.5]
        assert result == expected

    def test_parse_numbers_with_zero_strings_returns_zeros(self):
        """Test parse_numbers handles zero strings."""
        zero_strings = ["0", "0.0", "0.00"]
        result = parse_numbers(zero_strings)
        expected = [0.0, 0.0, 0.0]
        assert result == expected

    def test_parse_numbers_with_scientific_notation_returns_correct_floats(self):
        """Test parse_numbers handles scientific notation."""
        scientific_strings = ["1e2", "2.5e-3", "3.14e+1", "-1.5e-2"]
        result = parse_numbers(scientific_strings)
        expected = [100.0, 0.0025, 31.4, -0.015]

        # Use approximate comparison for floating point
        for actual, expected_val in zip(result, expected):
            assert abs(actual - expected_val) < 1e-10

    def test_parse_numbers_with_whitespace_strings_returns_correct_floats(self):
        """Test parse_numbers handles strings with whitespace."""
        whitespace_strings = [" 1.5 ", "\t2.0\t", "\n3.5\n", "  4.0  "]
        result = parse_numbers(whitespace_strings)
        expected = [1.5, 2.0, 3.5, 4.0]
        assert result == expected

    def test_parse_numbers_with_invalid_string_raises_value_error(
        self, invalid_string_list
    ):
        """Test parse_numbers raises ValueError for invalid strings."""
        with pytest.raises(ValueError, match="Could not parse"):
            parse_numbers(invalid_string_list)

    def test_parse_numbers_with_empty_string_raises_value_error(self):
        """Test parse_numbers raises ValueError for empty strings."""
        empty_strings = ["1.5", "", "3.5"]
        with pytest.raises(ValueError, match="Could not parse"):
            parse_numbers(empty_strings)

    def test_parse_numbers_with_non_numeric_string_raises_value_error(self):
        """Test parse_numbers raises ValueError for non-numeric strings."""
        non_numeric = ["1.5", "abc", "3.5"]
        with pytest.raises(ValueError, match="Could not parse"):
            parse_numbers(non_numeric)

    def test_parse_numbers_with_special_strings_raises_value_error(self):
        """Test parse_numbers raises ValueError for special strings."""
        special_strings = ["1.5", "inf", "3.5"]
        # Note: "inf" actually converts to float('inf'), so let's test with truly invalid strings
        special_strings = ["1.5", "not_a_number", "3.5"]
        with pytest.raises(ValueError, match="Could not parse"):
            parse_numbers(special_strings)

    def test_parse_numbers_with_empty_list_returns_empty_list(self):
        """Test parse_numbers with empty list returns empty list."""
        result = parse_numbers([])
        assert result == []

    def test_parse_numbers_with_single_string_returns_single_float(self):
        """Test parse_numbers with single string returns single float list."""
        result = parse_numbers(["42.5"])
        assert result == [42.5]

    def test_parse_numbers_preserves_precision(self):
        """Test parse_numbers preserves floating point precision."""
        precision_strings = ["3.141592653589793", "2.718281828459045"]
        result = parse_numbers(precision_strings)

        # Check that precision is maintained within reasonable limits
        assert abs(result[0] - 3.141592653589793) < 1e-15
        assert abs(result[1] - 2.718281828459045) < 1e-15

    def test_parse_numbers_with_very_large_numbers(self):
        """Test parse_numbers handles very large numbers."""
        large_strings = ["1e100", "9.999e99"]
        result = parse_numbers(large_strings)
        assert result[0] == 1e100
        assert result[1] == 9.999e99

    def test_parse_numbers_with_very_small_numbers(self):
        """Test parse_numbers handles very small numbers."""
        small_strings = ["1e-100", "9.999e-99"]
        result = parse_numbers(small_strings)
        assert result[0] == 1e-100
        assert result[1] == 9.999e-99

    def test_parse_numbers_with_none_raises_type_error(self):
        """Test parse_numbers raises TypeError when given None."""
        with pytest.raises(TypeError):
            parse_numbers(None)

    def test_parse_numbers_with_mixed_valid_formats(self):
        """Test parse_numbers with various valid number formats."""
        mixed_formats = ["42", "3.14", "-2.5", "1e-3", " 7.0 ", "0"]
        result = parse_numbers(mixed_formats)
        expected = [42.0, 3.14, -2.5, 0.001, 7.0, 0.0]

        for actual, expected_val in zip(result, expected):
            assert abs(actual - expected_val) < 1e-10
