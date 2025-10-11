"""Unit tests for mathematical operations (sum_five and multiply_six functions)."""

import os
import sys
from typing import List, Sequence

import pytest

# Add the parent directory to the path to import sum_five module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from sum_five import multiply_six, sum_five


class TestSumFive:
    """Test cases for the sum_five function."""

    def test_sum_five_with_positive_integers_returns_correct_sum(
        self, valid_five_numbers
    ):
        """Test sum_five correctly sums five positive numbers."""
        result = sum_five(valid_five_numbers)
        expected = 15.0  # 1 + 2 + 3 + 4 + 5
        assert result == expected

    def test_sum_five_with_zeros_returns_zero(self):
        """Test sum_five with all zeros returns zero."""
        zeros = [0.0, 0.0, 0.0, 0.0, 0.0]
        result = sum_five(zeros)
        assert result == 0.0

    def test_sum_five_with_negative_numbers_returns_correct_sum(self):
        """Test sum_five correctly handles negative numbers."""
        negative_numbers = [-1.0, -2.0, -3.0, -4.0, -5.0]
        result = sum_five(negative_numbers)
        expected = -15.0
        assert result == expected

    def test_sum_five_with_mixed_signs_returns_correct_sum(self):
        """Test sum_five with mix of positive and negative numbers."""
        mixed_numbers = [10.0, -5.0, 3.0, -2.0, 4.0]
        result = sum_five(mixed_numbers)
        expected = 10.0  # 10 - 5 + 3 - 2 + 4
        assert result == expected

    def test_sum_five_with_floating_point_numbers_returns_correct_sum(self):
        """Test sum_five with floating point numbers."""
        float_numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
        result = sum_five(float_numbers)
        expected = 17.5
        assert result == expected

    def test_sum_five_with_large_numbers_returns_correct_sum(self):
        """Test sum_five with very large numbers."""
        large_numbers = [1e10, 2e10, 3e10, 4e10, 5e10]
        result = sum_five(large_numbers)
        expected = 15e10
        assert result == expected

    def test_sum_five_with_very_small_numbers_returns_correct_sum(self):
        """Test sum_five with very small numbers."""
        small_numbers = [1e-10, 2e-10, 3e-10, 4e-10, 5e-10]
        result = sum_five(small_numbers)
        expected = 15e-10
        assert abs(result - expected) < 1e-15  # Account for floating point precision

    def test_sum_five_with_four_numbers_raises_value_error(self, invalid_four_numbers):
        """Test sum_five raises ValueError when given four numbers."""
        with pytest.raises(ValueError, match="requires exactly five values"):
            sum_five(invalid_four_numbers)

    def test_sum_five_with_six_numbers_raises_value_error(self):
        """Test sum_five raises ValueError when given six numbers."""
        six_numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
        with pytest.raises(ValueError, match="requires exactly five values"):
            sum_five(six_numbers)

    def test_sum_five_with_empty_list_raises_value_error(self):
        """Test sum_five raises ValueError when given empty list."""
        with pytest.raises(ValueError, match="requires exactly five values"):
            sum_five([])

    def test_sum_five_with_none_raises_type_error(self):
        """Test sum_five raises TypeError when given None."""
        with pytest.raises(TypeError):
            sum_five(None)

    def test_sum_five_preserves_input_type_properties(self):
        """Test sum_five works with different numeric types."""
        # Test with integers
        int_numbers = [1, 2, 3, 4, 5]
        result = sum_five(int_numbers)
        assert result == 15.0
        assert isinstance(result, float)

    def test_sum_five_with_tuple_input_works(self):
        """Test sum_five works with tuple input."""
        tuple_numbers = (1.0, 2.0, 3.0, 4.0, 5.0)
        result = sum_five(tuple_numbers)
        assert result == 15.0


class TestMultiplySix:
    """Test cases for the multiply_six function."""

    def test_multiply_six_with_positive_integers_returns_correct_product(
        self, valid_six_numbers
    ):
        """Test multiply_six correctly calculates product of six positive numbers."""
        result = multiply_six(valid_six_numbers)
        expected = 720.0  # 1 * 2 * 3 * 4 * 5 * 6
        assert result == expected

    def test_multiply_six_with_ones_returns_one(self):
        """Test multiply_six with all ones returns one."""
        ones = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        result = multiply_six(ones)
        assert result == 1.0

    def test_multiply_six_with_zero_returns_zero(self, six_numbers_with_zero):
        """Test multiply_six with any zero returns zero."""
        result = multiply_six(six_numbers_with_zero)
        assert result == 0.0

    def test_multiply_six_with_negative_numbers_returns_correct_product(self):
        """Test multiply_six correctly handles negative numbers."""
        negative_numbers = [-1.0, -2.0, -3.0, -4.0, -5.0, -6.0]
        result = multiply_six(negative_numbers)
        expected = 720.0  # Even number of negatives = positive result
        assert result == expected

    def test_multiply_six_with_odd_negatives_returns_negative_product(
        self, mixed_sign_six_numbers
    ):
        """Test multiply_six with odd number of negatives returns negative result."""
        # mixed_sign_six_numbers = [2.0, -3.0, 4.0, -5.0, 6.0, 7.0] (2 negatives = even)
        # Let's create a case with odd number of negatives
        odd_negative_numbers = [2.0, -3.0, 4.0, 5.0, 6.0, 7.0]  # 1 negative
        result = multiply_six(odd_negative_numbers)
        expected = -5040.0  # 2 * (-3) * 4 * 5 * 6 * 7 = -5040
        assert result == expected

    def test_multiply_six_with_floating_point_numbers_returns_correct_product(self):
        """Test multiply_six with floating point numbers."""
        float_numbers = [1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
        result = multiply_six(float_numbers)
        expected = 1.5 * 2.0 * 2.5 * 3.0 * 3.5 * 4.0
        assert abs(result - expected) < 1e-10  # Account for floating point precision

    def test_multiply_six_with_large_numbers_returns_correct_product(self):
        """Test multiply_six with large numbers."""
        large_numbers = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0]
        result = multiply_six(large_numbers)
        expected = 1e6  # 10^6
        assert result == expected

    def test_multiply_six_with_very_small_numbers_returns_correct_product(
        self, small_six_numbers
    ):
        """Test multiply_six with very small numbers."""
        result = multiply_six(small_six_numbers)
        expected = 0.1 * 0.2 * 0.3 * 0.4 * 0.5 * 0.6
        assert abs(result - expected) < 1e-15

    def test_multiply_six_with_five_numbers_raises_value_error(
        self, valid_five_numbers
    ):
        """Test multiply_six raises ValueError when given five numbers."""
        with pytest.raises(ValueError, match="requires exactly six values"):
            multiply_six(valid_five_numbers)

    def test_multiply_six_with_seven_numbers_raises_value_error(
        self, invalid_seven_numbers
    ):
        """Test multiply_six raises ValueError when given seven numbers."""
        with pytest.raises(ValueError, match="requires exactly six values"):
            multiply_six(invalid_seven_numbers)

    def test_multiply_six_with_empty_list_raises_value_error(self):
        """Test multiply_six raises ValueError when given empty list."""
        with pytest.raises(ValueError, match="requires exactly six values"):
            multiply_six([])

    def test_multiply_six_with_none_raises_type_error(self):
        """Test multiply_six raises TypeError when given None."""
        with pytest.raises(TypeError):
            multiply_six(None)

    def test_multiply_six_preserves_input_type_properties(self):
        """Test multiply_six works with different numeric types."""
        # Test with integers
        int_numbers = [1, 2, 3, 4, 5, 6]
        result = multiply_six(int_numbers)
        assert result == 720.0
        assert isinstance(result, float)

    def test_multiply_six_with_tuple_input_works(self):
        """Test multiply_six works with tuple input."""
        tuple_numbers = (1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
        result = multiply_six(tuple_numbers)
        assert result == 720.0

    def test_multiply_six_order_independence(self):
        """Test multiply_six result is independent of input order."""
        numbers1 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
        numbers2 = [6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
        numbers3 = [3.0, 1.0, 5.0, 2.0, 6.0, 4.0]

        result1 = multiply_six(numbers1)
        result2 = multiply_six(numbers2)
        result3 = multiply_six(numbers3)

        assert result1 == result2 == result3

    def test_multiply_six_identity_property(self):
        """Test multiply_six identity property with ones."""
        for x in [5.0, -3.0, 0.0, 100.0]:
            numbers = [1.0, 1.0, 1.0, 1.0, 1.0, x]
            result = multiply_six(numbers)
            assert result == x
