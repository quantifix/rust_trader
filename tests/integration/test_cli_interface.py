"""Integration tests for CLI interface functionality."""

import os
import subprocess
import sys
from typing import List

import pytest


class TestCLIInterface:
    """Test cases for the command-line interface."""

    def get_script_path(self) -> str:
        """Get the path to the sum_five.py script."""
        return os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "sum_five.py"
        )

    def run_cli(self, args: List[str]) -> subprocess.CompletedProcess:
        """Helper method to run the CLI with given arguments."""
        script_path = self.get_script_path()
        cmd = [sys.executable, script_path] + args
        return subprocess.run(cmd, capture_output=True, text=True)

    def test_cli_sum_operation_with_five_numbers_succeeds(self):
        """Test CLI sum operation with five valid numbers."""
        result = self.run_cli(["--operation", "sum", "1", "2", "3", "4", "5"])

        assert result.returncode == 0
        assert "15.0" in result.stdout
        assert result.stderr == ""

    def test_cli_multiply_operation_with_six_numbers_succeeds(self):
        """Test CLI multiply operation with six valid numbers."""
        result = self.run_cli(["--operation", "multiply", "1", "2", "3", "4", "5", "6"])

        assert result.returncode == 0
        assert "720.0" in result.stdout
        assert result.stderr == ""

    def test_cli_sum_operation_with_floating_point_numbers_succeeds(self):
        """Test CLI sum operation with floating point numbers."""
        result = self.run_cli(["--operation", "sum", "1.5", "2.5", "3.5", "4.5", "5.5"])

        assert result.returncode == 0
        assert "17.5" in result.stdout

    def test_cli_multiply_operation_with_floating_point_numbers_succeeds(self):
        """Test CLI multiply operation with floating point numbers."""
        result = self.run_cli(
            ["--operation", "multiply", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0"]
        )

        assert result.returncode == 0
        assert "720.0" in result.stdout

    def test_cli_sum_operation_with_negative_numbers_succeeds(self):
        """Test CLI sum operation with negative numbers."""
        result = self.run_cli(["--operation", "sum", "-1", "-2", "-3", "-4", "-5"])

        assert result.returncode == 0
        assert "-15.0" in result.stdout

    def test_cli_multiply_operation_with_negative_numbers_succeeds(self):
        """Test CLI multiply operation with negative numbers."""
        result = self.run_cli(
            ["--operation", "multiply", "-1", "2", "-3", "4", "-5", "6"]
        )

        assert result.returncode == 0
        # -1 * 2 * -3 * 4 * -5 * 6 = 720 (even number of negatives)
        assert "720.0" in result.stdout

    def test_cli_sum_operation_with_wrong_number_of_arguments_fails(self):
        """Test CLI sum operation fails with wrong number of arguments."""
        result = self.run_cli(
            ["--operation", "sum", "1", "2", "3", "4"]
        )  # Only 4 numbers

        assert result.returncode != 0
        assert "sum operation requires exactly 5 numbers" in result.stderr

    def test_cli_multiply_operation_with_wrong_number_of_arguments_fails(self):
        """Test CLI multiply operation fails with wrong number of arguments."""
        result = self.run_cli(
            ["--operation", "multiply", "1", "2", "3", "4", "5"]
        )  # Only 5 numbers

        assert result.returncode != 0
        assert "multiply operation requires exactly 6 numbers" in result.stderr

    def test_cli_with_invalid_operation_fails(self):
        """Test CLI fails with invalid operation."""
        result = self.run_cli(["--operation", "divide", "1", "2", "3", "4", "5"])

        assert result.returncode != 0
        assert "invalid choice" in result.stderr.lower()

    def test_cli_with_invalid_number_format_fails(self):
        """Test CLI fails with invalid number format."""
        result = self.run_cli(
            ["--operation", "sum", "1", "2", "not_a_number", "4", "5"]
        )

        assert result.returncode != 0
        assert "invalid float value" in result.stderr

    def test_cli_with_no_arguments_shows_help(self):
        """Test CLI shows help when no arguments provided."""
        result = self.run_cli([])

        assert result.returncode != 0
        # Should show usage information
        assert "usage:" in result.stderr.lower() or "error:" in result.stderr.lower()

    def test_cli_with_help_flag_shows_help(self):
        """Test CLI shows help with --help flag."""
        result = self.run_cli(["--help"])

        assert result.returncode == 0
        assert "usage:" in result.stdout.lower()
        assert "operation" in result.stdout.lower()

    def test_cli_sum_operation_with_scientific_notation_succeeds(self):
        """Test CLI sum operation with scientific notation."""
        result = self.run_cli(["--operation", "sum", "1e1", "2e1", "3e1", "4e1", "5e1"])

        assert result.returncode == 0
        assert "150.0" in result.stdout  # 10 + 20 + 30 + 40 + 50

    def test_cli_multiply_operation_with_zeros_returns_zero(self):
        """Test CLI multiply operation with zeros returns zero."""
        result = self.run_cli(["--operation", "multiply", "0", "1", "2", "3", "4", "5"])

        assert result.returncode == 0
        assert "0.0" in result.stdout

    def test_cli_sum_operation_with_large_numbers_succeeds(self):
        """Test CLI sum operation with large numbers."""
        result = self.run_cli(
            [
                "--operation",
                "sum",
                "1000000",
                "2000000",
                "3000000",
                "4000000",
                "5000000",
            ]
        )

        assert result.returncode == 0
        assert "15000000.0" in result.stdout

    def test_cli_multiply_operation_with_ones_returns_one(self):
        """Test CLI multiply operation with all ones returns one."""
        result = self.run_cli(["--operation", "multiply", "1", "1", "1", "1", "1", "1"])

        assert result.returncode == 0
        assert "1.0" in result.stdout

    def test_cli_backward_compatibility_sum_without_operation_flag(self):
        """Test CLI maintains backward compatibility for sum operation without --operation flag."""
        result = self.run_cli(["1", "2", "3", "4", "5"])

        assert result.returncode == 0
        assert "15.0" in result.stdout

    def test_cli_backward_compatibility_with_wrong_number_fails(self):
        """Test CLI backward compatibility fails with wrong number of arguments."""
        result = self.run_cli(["1", "2", "3", "4"])  # Only 4 numbers for sum

        assert result.returncode != 0
        assert "sum operation requires exactly 5 numbers" in result.stderr

    def test_cli_output_format_consistency(self):
        """Test CLI output format is consistent across operations."""
        sum_result = self.run_cli(["--operation", "sum", "1", "2", "3", "4", "5"])
        multiply_result = self.run_cli(
            ["--operation", "multiply", "1", "2", "3", "4", "5", "6"]
        )

        assert sum_result.returncode == 0
        assert multiply_result.returncode == 0

        # Both should output floating point numbers
        assert ".0" in sum_result.stdout
        assert ".0" in multiply_result.stdout

    def test_cli_error_message_clarity(self):
        """Test CLI provides clear error messages."""
        # Test with wrong number of arguments
        result = self.run_cli(["--operation", "sum", "1", "2", "3"])

        assert result.returncode != 0
        error_msg = result.stderr.lower()
        assert "sum operation requires exactly 5 numbers" in error_msg

        # Test with invalid number
        result = self.run_cli(["--operation", "sum", "1", "2", "abc", "4", "5"])

        assert result.returncode != 0
        error_msg = result.stderr.lower()
        assert "could not convert" in error_msg or "invalid" in error_msg

    def test_cli_handles_edge_case_numbers(self):
        """Test CLI handles edge case numbers correctly."""
        # Test with very small numbers
        result = self.run_cli(["--operation", "sum", "0.1", "0.2", "0.3", "0.4", "0.5"])
        assert result.returncode == 0
        assert "1.5" in result.stdout

        # Test with negative zero
        result = self.run_cli(
            ["--operation", "multiply", "-0", "1", "2", "3", "4", "5"]
        )
        assert result.returncode == 0
        assert "0.0" in result.stdout or "-0.0" in result.stdout
