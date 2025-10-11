# AI Agent Testing Quick Reference

## 🤖 MANDATORY Requirements for AI Agents

### Before Writing ANY Code
1. **READ** `TESTING_STRATEGY.md` and `TESTING_DECISIONS.md`
2. **UNDERSTAND** the testing philosophy and requirements
3. **PLAN** your testing approach before implementation

### For Every New Function/Feature
```python
# ❌ WRONG: Implement first, test later
def new_function():
    return "implementation"

# ✅ CORRECT: Test first, then implement
def test_new_function_basic_case():
    """Test new_function with basic input."""
    result = new_function("input")
    assert result == "expected"

def test_new_function_edge_case():
    """Test new_function with edge case."""
    with pytest.raises(ValueError):
        new_function(None)

def new_function(input_data):
    """Implementation goes here."""
    if input_data is None:
        raise ValueError("Input cannot be None")
    return "implementation"
```

### Coverage Requirements (NON-NEGOTIABLE)
- **Business Logic**: 95% minimum
- **CLI Functions**: 80% minimum  
- **Overall Project**: 90% minimum
- **MUST** verify coverage before committing

### Test Organization Rules
```
tests/
├── unit/           # Test individual functions
├── integration/    # Test component interactions  
├── property/       # Test mathematical properties
└── conftest.py     # Shared fixtures
```

## 🚨 Critical Checkpoints

### Before Every Commit
```bash
# 1. Run all tests
pytest

# 2. Check coverage
pytest --cov=. --cov-report=term-missing

# 3. Verify coverage meets minimums
# Business logic: 95%+
# CLI: 80%+
# Overall: 90%+
```

### Test Naming Convention
```python
def test_<function_name>_<scenario>_<expected_outcome>():
    """Brief description of what is being tested."""
```

Examples:
```python
def test_multiply_six_with_valid_input_returns_product():
def test_multiply_six_with_five_numbers_raises_value_error():
def test_sum_five_with_zeros_returns_zero():
```

## 📝 Test Writing Patterns

### Unit Test Template
```python
def test_function_name_scenario():
    """Test that function_name does X when given Y.
    
    This test verifies [business rule or requirement].
    """
    # Arrange
    input_data = [1, 2, 3, 4, 5, 6]
    expected = 720
    
    # Act
    result = multiply_six(input_data)
    
    # Assert
    assert result == expected
```

### Error Testing Template
```python
def test_function_name_invalid_input_raises_error():
    """Test that function_name raises ValueError for invalid input."""
    with pytest.raises(ValueError, match="specific error message"):
        function_name(invalid_input)
```

### Property-Based Test Template
```python
from hypothesis import given, strategies as st

@given(st.lists(st.floats(min_value=-1000, max_value=1000), 
                min_size=6, max_size=6))
def test_multiply_six_property(numbers):
    """Test mathematical property of multiply_six."""
    result = multiply_six(numbers)
    # Test some mathematical property
    assert isinstance(result, float)
```

## 🔍 Common Testing Scenarios

### Mathematical Functions
```python
# Test normal cases
def test_with_positive_numbers():
def test_with_negative_numbers():
def test_with_mixed_signs():
def test_with_zeros():
def test_with_ones():

# Test edge cases  
def test_with_very_large_numbers():
def test_with_very_small_numbers():
def test_with_floating_point_precision():

# Test error conditions
def test_with_wrong_number_of_arguments():
def test_with_non_numeric_input():
def test_with_none_input():
```

### CLI Functions
```python
import subprocess

def test_cli_with_valid_arguments():
    """Test CLI with valid arguments."""
    result = subprocess.run(
        ["python", "sum_five.py", "1", "2", "3", "4", "5"],
        capture_output=True, text=True
    )
    assert result.returncode == 0
    assert "15.0" in result.stdout

def test_cli_with_invalid_arguments():
    """Test CLI with invalid arguments."""
    result = subprocess.run(
        ["python", "sum_five.py", "1", "2", "3"],
        capture_output=True, text=True
    )
    assert result.returncode != 0
    assert "error" in result.stderr.lower()
```

## ⚠️ Common Mistakes to Avoid

### ❌ DON'T DO THIS
```python
# Vague test names
def test_function():
def test_error():

# No docstrings
def test_multiply_six():
    assert multiply_six([1,2,3,4,5,6]) == 720

# Testing implementation details
def test_multiply_six_uses_loop():
    # Don't test HOW it works, test WHAT it does

# Ignoring edge cases
def test_multiply_six():
    assert multiply_six([1,2,3,4,5,6]) == 720
    # Missing: zeros, negatives, large numbers, etc.
```

### ✅ DO THIS INSTEAD
```python
# Clear, descriptive names
def test_multiply_six_with_positive_integers_returns_correct_product():
def test_multiply_six_with_insufficient_arguments_raises_value_error():

# Good docstrings
def test_multiply_six_with_positive_integers_returns_correct_product():
    """Test multiply_six correctly calculates product of six positive integers.
    
    Verifies basic multiplication functionality with simple positive integers.
    """
    result = multiply_six([1, 2, 3, 4, 5, 6])
    assert result == 720

# Test behavior, not implementation
def test_multiply_six_result_properties():
    """Test mathematical properties of multiply_six result."""
    # Test what the function should do, not how

# Comprehensive edge cases
def test_multiply_six_comprehensive():
    """Test multiply_six with various input scenarios."""
    # Positive numbers
    assert multiply_six([1, 2, 3, 4, 5, 6]) == 720
    # With zero
    assert multiply_six([0, 1, 2, 3, 4, 5]) == 0
    # With negatives
    assert multiply_six([-1, 2, 3, 4, 5, 6]) == -720
```

## 🎯 Quality Checklist

Before marking any task complete, verify:

- [ ] All new functions have corresponding tests
- [ ] Tests cover happy path, edge cases, and error conditions
- [ ] Test names are descriptive and follow naming convention
- [ ] All tests have docstrings explaining what they test
- [ ] Coverage meets minimum requirements (90%+ overall)
- [ ] All tests pass locally
- [ ] No flaky or non-deterministic tests
- [ ] Property-based tests for mathematical functions
- [ ] CLI integration tests if applicable

## 🚀 Quick Commands

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run only unit tests
pytest tests/unit/

# Run specific test file
pytest tests/unit/test_mathematical_operations.py

# Run tests matching pattern
pytest -k "multiply_six"

# Run with verbose output
pytest -v

# Run and stop on first failure
pytest -x
```

## 📞 When in Doubt

1. **Check existing tests** for patterns and examples
2. **Refer to TESTING_STRATEGY.md** for detailed guidelines
3. **Review TESTING_DECISIONS.md** for context on why decisions were made
4. **Write more tests rather than fewer** - err on the side of thorough testing
5. **Ask for clarification** if requirements are unclear

## 🎓 Learning Resources

- [pytest documentation](https://docs.pytest.org/)
- [hypothesis documentation](https://hypothesis.readthedocs.io/)
- [Python testing best practices](https://realpython.com/python-testing/)

---

**Remember**: Good tests are an investment in code quality, maintainability, and developer confidence. Take the time to write them well!