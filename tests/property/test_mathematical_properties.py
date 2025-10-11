"""Property-based tests for mathematical functions using hypothesis."""

import os
import sys
from typing import List

import pytest
from hypothesis import assume, given
from hypothesis import strategies as st

# Add the parent directory to the path to import sum_five module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from sum_five import multiply_six, sum_five


class TestSumFiveProperties:
    """Property-based tests for sum_five function."""

    @given(
        st.lists(
            st.floats(
                min_value=-1e6, max_value=1e6, allow_nan=False, allow_infinity=False
            ),
            min_size=5,
            max_size=5,
        )
    )
    def test_sum_five_commutative_property(self, numbers: List[float]):
        """Test that sum_five is commutative (order doesn't matter)."""
        # Create a different permutation of the same numbers
        reversed_numbers = list(reversed(numbers))

        result1 = sum_five(numbers)
        result2 = sum_five(reversed_numbers)

        # Should be equal within floating point precision
        assert abs(result1 - result2) < 1e-10

    @given(
        st.lists(
            st.floats(
                min_value=-1e6, max_value=1e6, allow_nan=False, allow_infinity=False
            ),
            min_size=5,
            max_size=5,
        )
    )
    def test_sum_five_associative_property(self, numbers: List[float]):
        """Test associative property: (a+b)+c = a+(b+c) for sum_five."""
        # For sum_five, we can test that the sum equals the built-in sum
        result = sum_five(numbers)
        expected = sum(numbers)

        # Should be equal within floating point precision
        assert abs(result - expected) < 1e-10

    @given(
        st.lists(
            st.floats(
                min_value=-1e3, max_value=1e3, allow_nan=False, allow_infinity=False
            ),
            min_size=5,
            max_size=5,
        )
    )
    def test_sum_five_identity_property(self, numbers: List[float]):
        """Test identity property: adding zero doesn't change the sum."""
        # Replace one number with zero and adjust another to maintain the same sum
        original_sum = sum_five(numbers)

        # Create a new list where we add zero and subtract it from another element
        modified_numbers = numbers.copy()
        if len(modified_numbers) >= 2:
            modified_numbers[0] = modified_numbers[0] + modified_numbers[1]
            modified_numbers[1] = 0.0

            result = sum_five(modified_numbers)
            # Use relative error for better floating point comparison
            relative_error = abs(result - original_sum) / (abs(original_sum) + 1e-10)
            assert relative_error < 1e-8

    @given(
        st.lists(
            st.floats(
                min_value=-1e3, max_value=1e3, allow_nan=False, allow_infinity=False
            ),
            min_size=5,
            max_size=5,
        )
    )
    def test_sum_five_scaling_property(self, numbers: List[float]):
        """Test scaling property: sum(k*numbers) = k*sum(numbers)."""
        k = 2.5  # scaling factor

        original_sum = sum_five(numbers)
        scaled_numbers = [k * x for x in numbers]
        scaled_sum = sum_five(scaled_numbers)

        expected_scaled_sum = k * original_sum

        # Should be equal within floating point precision
        assert abs(scaled_sum - expected_scaled_sum) < 1e-8

    @given(
        st.lists(
            st.floats(
                min_value=-100, max_value=100, allow_nan=False, allow_infinity=False
            ),
            min_size=5,
            max_size=5,
        )
    )
    def test_sum_five_always_returns_float(self, numbers: List[float]):
        """Test that sum_five always returns a float."""
        result = sum_five(numbers)
        assert isinstance(result, float)

    @given(
        st.lists(st.integers(min_value=-1000, max_value=1000), min_size=5, max_size=5)
    )
    def test_sum_five_with_integers_returns_float(self, numbers: List[int]):
        """Test that sum_five returns float even with integer input."""
        result = sum_five(numbers)
        assert isinstance(result, float)
        assert result == float(sum(numbers))


class TestMultiplySixProperties:
    """Property-based tests for multiply_six function."""

    def test_multiply_six_commutative_property_specific_cases(self):
        """Test that multiply_six is commutative (order doesn't matter)."""
        import random

        test_cases = [
            [1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
            [-1.0, 2.0, -3.0, 4.0, -5.0, 6.0],
            [0.5, 1.5, 2.5, 3.5, 4.5, 5.5],
            [10.0, 20.0, 30.0, 40.0, 50.0, 60.0],
        ]

        for numbers in test_cases:
            # Create different permutations
            reversed_numbers = list(reversed(numbers))
            sorted_numbers = sorted(numbers)
            shuffled_numbers = numbers.copy()
            random.shuffle(shuffled_numbers)

            result1 = multiply_six(numbers)
            result2 = multiply_six(reversed_numbers)
            result3 = multiply_six(sorted_numbers)
            result4 = multiply_six(shuffled_numbers)

            # All results should be equal within floating point precision
            assert abs(result1 - result2) < 1e-10
            assert abs(result1 - result3) < 1e-10
            assert abs(result1 - result4) < 1e-10

    @given(
        st.lists(
            st.floats(
                min_value=-10, max_value=10, allow_nan=False, allow_infinity=False
            ),
            min_size=6,
            max_size=6,
        )
    )
    def test_multiply_six_zero_property(self, numbers: List[float]):
        """Test that multiply_six returns zero if any input is zero."""
        # Replace one number with zero
        numbers_with_zero = numbers.copy()
        numbers_with_zero[0] = 0.0

        result = multiply_six(numbers_with_zero)
        assert result == 0.0

    @given(
        st.lists(
            st.floats(
                min_value=-10, max_value=10, allow_nan=False, allow_infinity=False
            ),
            min_size=6,
            max_size=6,
        )
    )
    def test_multiply_six_identity_property(self, numbers: List[float]):
        """Test identity property: multiplying by one doesn't change the product."""
        # Skip if any number is zero to avoid trivial cases
        assume(all(x != 0.0 for x in numbers))

        # Replace one number with 1 and multiply another by the original value
        original_product = multiply_six(numbers)

        modified_numbers = numbers.copy()
        if abs(modified_numbers[1]) > 1e-10:  # Avoid division by very small numbers
            modified_numbers[0] = modified_numbers[0] * modified_numbers[1]
            modified_numbers[1] = 1.0

            result = multiply_six(modified_numbers)

            # Should be equal within floating point precision
            relative_error = abs(result - original_product) / (
                abs(original_product) + 1e-10
            )
            assert relative_error < 1e-8

    @given(
        st.lists(
            st.floats(min_value=1, max_value=10, allow_nan=False, allow_infinity=False),
            min_size=6,
            max_size=6,
        )
    )
    def test_multiply_six_sign_property(self, positive_numbers: List[float]):
        """Test sign properties of multiply_six."""
        # All positive numbers should give positive result
        result_positive = multiply_six(positive_numbers)
        assert result_positive > 0

        # Even number of negative numbers should give positive result
        numbers_even_negative = positive_numbers.copy()
        numbers_even_negative[0] = -numbers_even_negative[0]
        numbers_even_negative[1] = -numbers_even_negative[1]  # 2 negatives (even)

        result_even_negative = multiply_six(numbers_even_negative)
        assert result_even_negative > 0

        # Odd number of negative numbers should give negative result
        numbers_odd_negative = positive_numbers.copy()
        numbers_odd_negative[0] = -numbers_odd_negative[0]  # 1 negative (odd)

        result_odd_negative = multiply_six(numbers_odd_negative)
        assert result_odd_negative < 0

    @given(
        st.lists(
            st.floats(
                min_value=-10, max_value=10, allow_nan=False, allow_infinity=False
            ),
            min_size=6,
            max_size=6,
        )
    )
    def test_multiply_six_always_returns_float(self, numbers: List[float]):
        """Test that multiply_six always returns a float."""
        result = multiply_six(numbers)
        assert isinstance(result, float)

    @given(st.lists(st.integers(min_value=-10, max_value=10), min_size=6, max_size=6))
    def test_multiply_six_with_integers_returns_float(self, numbers: List[int]):
        """Test that multiply_six returns float even with integer input."""
        result = multiply_six(numbers)
        assert isinstance(result, float)

    @given(
        st.lists(
            st.floats(
                min_value=0.1, max_value=2.0, allow_nan=False, allow_infinity=False
            ),
            min_size=6,
            max_size=6,
        )
    )
    def test_multiply_six_scaling_property(self, numbers: List[float]):
        """Test scaling property: multiply_six(k*numbers) = k^6 * multiply_six(numbers)."""
        k = 2.0  # scaling factor

        original_product = multiply_six(numbers)
        scaled_numbers = [k * x for x in numbers]
        scaled_product = multiply_six(scaled_numbers)

        expected_scaled_product = (k**6) * original_product

        # Should be equal within floating point precision
        relative_error = abs(scaled_product - expected_scaled_product) / (
            abs(expected_scaled_product) + 1e-10
        )
        assert relative_error < 1e-8

    def test_multiply_six_reciprocal_property_specific_cases(self):
        """Test reciprocal property with specific test cases."""
        # Test with simple cases that we know work
        test_cases = [
            [1.0, 2.0, 1.0, 2.0, 1.0, 2.0],  # Simple case
            [2.0, 2.0, 2.0, 2.0, 2.0, 2.0],  # All same values
            [-1.0, 2.0, -1.0, 2.0, -1.0, 2.0],  # With negatives
        ]

        for numbers in test_cases:
            original_product = multiply_six(numbers)
            reciprocal_numbers = [1.0 / x for x in numbers]
            reciprocal_product = multiply_six(reciprocal_numbers)

            expected_reciprocal = 1.0 / original_product

            # Should be equal within floating point precision
            relative_error = abs(reciprocal_product - expected_reciprocal) / (
                abs(expected_reciprocal) + 1e-10
            )
            assert relative_error < 1e-10


class TestCombinedProperties:
    """Property-based tests for combined behavior of both functions."""

    @given(
        st.lists(
            st.floats(
                min_value=-10, max_value=10, allow_nan=False, allow_infinity=False
            ),
            min_size=11,
            max_size=11,
        )
    )
    def test_functions_work_with_overlapping_data(self, eleven_numbers: List[float]):
        """Test that both functions work correctly with overlapping data sets."""
        # Use first 5 numbers for sum_five
        sum_numbers = eleven_numbers[:5]
        # Use last 6 numbers for multiply_six
        multiply_numbers = eleven_numbers[5:]

        sum_result = sum_five(sum_numbers)
        multiply_result = multiply_six(multiply_numbers)

        # Both should return floats
        assert isinstance(sum_result, float)
        assert isinstance(multiply_result, float)

        # Results should be finite (not inf or nan)
        assert abs(sum_result) < float("inf")
        if all(x != 0 for x in multiply_numbers):
            assert abs(multiply_result) < float("inf")

    @given(
        st.lists(
            st.floats(
                min_value=1.5, max_value=3, allow_nan=False, allow_infinity=False
            ),
            min_size=6,
            max_size=6,
        )
    )
    def test_multiply_six_grows_faster_than_sum_five(self, numbers: List[float]):
        """Test that multiply_six generally grows faster than sum_five for numbers > 1.5."""
        # Use same numbers for both (taking first 5 for sum)
        sum_numbers = numbers[:5]

        sum_result = sum_five(sum_numbers)
        multiply_result = multiply_six(numbers)

        # For numbers > 1.5, multiplication should generally be larger than sum
        # This is more reliable than testing with numbers close to 1
        if all(x >= 1.5 for x in numbers):
            assert multiply_result >= sum_result
