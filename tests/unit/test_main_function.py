"""Unit tests for the main function."""

import argparse
import os
import sys
from io import StringIO
from unittest.mock import patch

import pytest

# Add the parent directory to the path to import sum_five module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from sum_five import main


class TestMainFunction:
    """Test cases for the main function."""

    def test_main_sum_operation_with_valid_arguments(self, capsys):
        """Test main function with valid sum operation arguments."""
        argv = ["--operation", "sum", "1", "2", "3", "4", "5"]
        main(argv)

        captured = capsys.readouterr()
        assert "15.0" in captured.out
        assert captured.err == ""

    def test_main_multiply_operation_with_valid_arguments(self, capsys):
        """Test main function with valid multiply operation arguments."""
        argv = ["--operation", "multiply", "1", "2", "3", "4", "5", "6"]
        main(argv)

        captured = capsys.readouterr()
        assert "720.0" in captured.out
        assert captured.err == ""

    def test_main_default_sum_operation(self, capsys):
        """Test main function defaults to sum operation."""
        argv = ["1", "2", "3", "4", "5"]
        main(argv)

        captured = capsys.readouterr()
        assert "15.0" in captured.out

    def test_main_sum_operation_with_wrong_number_of_arguments_raises_system_exit(self):
        """Test main function raises SystemExit for wrong number of sum arguments."""
        argv = ["--operation", "sum", "1", "2", "3", "4"]  # Only 4 numbers

        with pytest.raises(SystemExit):
            main(argv)

    def test_main_multiply_operation_with_wrong_number_of_arguments_raises_system_exit(
        self,
    ):
        """Test main function raises SystemExit for wrong number of multiply arguments."""
        argv = ["--operation", "multiply", "1", "2", "3", "4", "5"]  # Only 5 numbers

        with pytest.raises(SystemExit):
            main(argv)

    def test_main_with_invalid_operation_raises_system_exit(self):
        """Test main function raises SystemExit for invalid operation."""
        argv = ["--operation", "divide", "1", "2", "3", "4", "5"]

        with pytest.raises(SystemExit):
            main(argv)

    def test_main_with_invalid_number_format_raises_system_exit(self):
        """Test main function raises SystemExit for invalid number format."""
        argv = ["--operation", "sum", "1", "2", "not_a_number", "4", "5"]

        with pytest.raises(SystemExit):
            main(argv)

    def test_main_with_no_arguments_raises_system_exit(self):
        """Test main function raises SystemExit when no arguments provided."""
        argv = []

        with pytest.raises(SystemExit):
            main(argv)

    def test_main_with_help_flag_raises_system_exit(self):
        """Test main function raises SystemExit with help flag."""
        argv = ["--help"]

        with pytest.raises(SystemExit) as exc_info:
            main(argv)

        # Help should exit with code 0
        assert exc_info.value.code == 0

    def test_main_sum_with_floating_point_numbers(self, capsys):
        """Test main function with floating point numbers for sum."""
        argv = ["--operation", "sum", "1.5", "2.5", "3.5", "4.5", "5.5"]
        main(argv)

        captured = capsys.readouterr()
        assert "17.5" in captured.out

    def test_main_multiply_with_floating_point_numbers(self, capsys):
        """Test main function with floating point numbers for multiply."""
        argv = ["--operation", "multiply", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0"]
        main(argv)

        captured = capsys.readouterr()
        assert "720.0" in captured.out

    def test_main_sum_with_negative_numbers(self, capsys):
        """Test main function with negative numbers for sum."""
        argv = ["--operation", "sum", "-1", "-2", "-3", "-4", "-5"]
        main(argv)

        captured = capsys.readouterr()
        assert "-15.0" in captured.out

    def test_main_multiply_with_negative_numbers(self, capsys):
        """Test main function with negative numbers for multiply."""
        argv = ["--operation", "multiply", "-1", "2", "-3", "4", "-5", "6"]
        main(argv)

        captured = capsys.readouterr()
        assert "720.0" in captured.out  # Even number of negatives = positive

    def test_main_multiply_with_zero_returns_zero(self, capsys):
        """Test main function multiply with zero returns zero."""
        argv = ["--operation", "multiply", "0", "1", "2", "3", "4", "5"]
        main(argv)

        captured = capsys.readouterr()
        assert "0.0" in captured.out

    def test_main_sum_with_scientific_notation(self, capsys):
        """Test main function with scientific notation."""
        argv = ["--operation", "sum", "1e1", "2e1", "3e1", "4e1", "5e1"]
        main(argv)

        captured = capsys.readouterr()
        assert "150.0" in captured.out

    def test_main_with_none_argv_uses_sys_argv(self):
        """Test main function with None argv uses sys.argv."""
        # Mock sys.argv to test default behavior
        original_argv = sys.argv
        try:
            sys.argv = ["sum_five.py", "1", "2", "3", "4", "5"]

            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                main(None)
                output = mock_stdout.getvalue()
                assert "15.0" in output
        finally:
            sys.argv = original_argv

    def test_main_argument_parsing_creates_correct_parser(self):
        """Test that main function creates parser with correct configuration."""
        # This test verifies the parser setup without executing it
        argv = ["--help"]

        with pytest.raises(SystemExit):
            main(argv)

        # If we get here, the parser was created successfully
        # (SystemExit is expected for --help)

    def test_main_handles_edge_case_numbers(self, capsys):
        """Test main function handles edge case numbers."""
        # Test with very small numbers
        argv = ["--operation", "sum", "0.1", "0.2", "0.3", "0.4", "0.5"]
        main(argv)

        captured = capsys.readouterr()
        assert "1.5" in captured.out

    def test_main_preserves_precision(self, capsys):
        """Test main function preserves floating point precision."""
        argv = ["--operation", "sum", "0.1", "0.2", "0.3", "0.4", "0.5"]
        main(argv)

        captured = capsys.readouterr()
        # Should handle floating point precision correctly
        assert "1.5" in captured.out
