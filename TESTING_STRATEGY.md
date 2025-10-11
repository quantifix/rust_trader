# Testing Strategy & Best Practices

## 📋 Overview

This document defines the testing strategy, standards, and best practices for the rust_trader project. All contributors (human developers and AI agents) MUST follow these guidelines to ensure code quality, maintainability, and reliability.

## 🎯 Testing Philosophy

### Core Principles
1. **Test-First Mindset**: Write tests before or alongside implementation
2. **Comprehensive Coverage**: Aim for high test coverage with meaningful tests
3. **Fast Feedback**: Tests should run quickly to enable rapid development
4. **Clear Intent**: Tests should serve as living documentation
5. **Maintainable**: Tests should be easy to understand and modify

### Quality Gates
- **Minimum Coverage**: 90% line coverage for all business logic
- **Test Types**: Unit, integration, and property-based tests required
- **Performance**: Test suite must complete in under 30 seconds
- **Reliability**: Tests must be deterministic and not flaky

## 🛠 Technology Stack Decisions

### Primary Testing Framework: **pytest**
**Decision**: Use pytest as the primary testing framework

**Rationale**:
- Industry standard with excellent ecosystem
- Superior test discovery and reporting
- Powerful fixture system for test setup/teardown
- Extensive plugin ecosystem (coverage, parallel execution, etc.)
- Better assertion introspection than unittest

**Consequences**:
- ✅ More readable and concise test code
- ✅ Better error messages and debugging
- ✅ Easier to extend with plugins
- ❌ External dependency (not in stdlib)
- ❌ Learning curve for unittest-familiar developers

### Test Coverage Tool: **coverage.py + pytest-cov**
**Decision**: Use coverage.py with pytest-cov plugin

**Rationale**:
- De facto standard for Python coverage measurement
- Integrates seamlessly with pytest
- Supports branch coverage, not just line coverage
- HTML and terminal reporting options

### Property-Based Testing: **hypothesis**
**Decision**: Use hypothesis for property-based testing of mathematical functions

**Rationale**:
- Excellent for testing mathematical properties
- Finds edge cases humans might miss
- Shrinks failing examples to minimal cases
- Integrates well with pytest

## 📁 Project Structure

```
rust_trader/
├── src/                          # Source code (future: when we add more modules)
│   └── rust_trader/
│       ├── __init__.py
│       └── core.py               # Renamed from sum_five.py
├── tests/                        # All test files
│   ├── __init__.py
│   ├── conftest.py              # Shared fixtures and configuration
│   ├── unit/                    # Unit tests
│   │   ├── __init__.py
│   │   ├── test_mathematical_operations.py
│   │   └── test_input_parsing.py
│   ├── integration/             # Integration tests
│   │   ├── __init__.py
│   │   └── test_cli_interface.py
│   └── property/                # Property-based tests
│       ├── __init__.py
│       └── test_mathematical_properties.py
├── pytest.ini                   # Pytest configuration
├── pyproject.toml               # Project metadata and tool configuration
├── requirements.txt             # Production dependencies
├── requirements-dev.txt         # Development dependencies
└── .github/
    └── workflows/
        └── test.yml             # CI/CD pipeline
```

## 🧪 Test Categories & Standards

### 1. Unit Tests
**Purpose**: Test individual functions in isolation

**Standards**:
- One test file per source module
- Test function naming: `test_<function_name>_<scenario>`
- Use descriptive test names that explain the scenario
- Test both happy path and error conditions
- Mock external dependencies

**Example Structure**:
```python
def test_sum_five_with_valid_input_returns_correct_sum():
    """Test that sum_five correctly sums five valid numbers."""
    
def test_sum_five_with_four_numbers_raises_value_error():
    """Test that sum_five raises ValueError when given four numbers."""
```

### 2. Integration Tests
**Purpose**: Test component interactions and CLI behavior

**Standards**:
- Test realistic user workflows
- Use subprocess for CLI testing
- Verify both stdout and exit codes
- Test error scenarios and edge cases

### 3. Property-Based Tests
**Purpose**: Test mathematical properties and invariants

**Standards**:
- Use hypothesis for generating test data
- Focus on mathematical properties (commutativity, associativity, etc.)
- Test with edge cases (zeros, negatives, very large numbers)
- Verify invariants hold across different inputs

**Example Properties to Test**:
- `multiply_six([a,b,c,d,e,f]) == multiply_six([f,e,d,c,b,a])` (order independence)
- `multiply_six([1,1,1,1,1,x]) == x` (identity property)
- `multiply_six([0,a,b,c,d,e]) == 0` (zero property)

## 📊 Coverage Requirements

### Minimum Coverage Targets
- **Overall Project**: 90% line coverage
- **Business Logic Functions**: 95% line coverage
- **CLI Interface**: 80% line coverage (excluding error handling)
- **Branch Coverage**: 85% for all conditional logic

### Coverage Exclusions
```python
# Acceptable exclusions (use sparingly):
if __name__ == "__main__":  # pragma: no cover
    main()

# Defensive error handling
except ImportError:  # pragma: no cover
    # fallback implementation
```

### Coverage Reporting
- Generate HTML reports for detailed analysis
- Fail CI if coverage drops below thresholds
- Track coverage trends over time

## 🚀 Continuous Integration

### GitHub Actions Workflow Requirements
1. **Multi-Python Testing**: Test on Python 3.8, 3.9, 3.10, 3.11, 3.12
2. **Operating Systems**: Test on Ubuntu, Windows, macOS
3. **Dependency Testing**: Test with minimum and latest dependency versions
4. **Coverage Reporting**: Upload coverage to codecov or similar service
5. **Performance Regression**: Fail if tests take >30 seconds

### Quality Gates
- All tests must pass
- Coverage must meet minimum thresholds
- No security vulnerabilities in dependencies
- Code style checks must pass (black, flake8, mypy)

## 🔧 Development Workflow

### Pre-commit Requirements
1. Run full test suite
2. Check code coverage
3. Run linting and formatting
4. Type checking with mypy

### Test-Driven Development (TDD)
**MANDATORY for new features**:
1. Write failing test first
2. Implement minimal code to pass
3. Refactor while keeping tests green
4. Add additional test cases for edge cases

### AI Agent Guidelines
**When implementing new features, AI agents MUST**:
1. Create tests BEFORE implementing functionality
2. Ensure all tests pass before committing
3. Verify coverage meets minimum thresholds
4. Update this document if testing strategy changes
5. Document any testing decisions in commit messages

## 📝 Test Documentation Standards

### Test Docstrings
```python
def test_multiply_six_with_mixed_positive_negative():
    """Test multiply_six with mix of positive and negative numbers.
    
    This test verifies that the function correctly handles the mathematical
    property that an odd number of negative values results in a negative product.
    
    Expected behavior:
    - Input: [2, -3, 4, -5, 6, 7]
    - Expected: negative result
    - Actual calculation: 2 * (-3) * 4 * (-5) * 6 * 7 = 5040
    """
```

### Test Comments
- Explain WHY a test exists, not WHAT it does
- Document business rules being tested
- Explain complex test setup or assertions
- Reference bug reports or requirements

## 🚨 Error Handling Testing

### Exception Testing Standards
```python
def test_function_raises_specific_exception():
    """Test that function raises ValueError with specific message."""
    with pytest.raises(ValueError, match="requires exactly six values"):
        multiply_six([1, 2, 3, 4, 5])  # Only 5 values
```

### Error Message Testing
- Verify exact error messages for user-facing errors
- Test error message formatting and clarity
- Ensure error messages provide actionable guidance

## 📈 Performance Testing

### Benchmarking Requirements
- Benchmark mathematical operations with large datasets
- Set performance regression thresholds
- Test memory usage for large inputs
- Document performance characteristics

### Performance Test Examples
```python
def test_multiply_six_performance_large_numbers():
    """Verify multiply_six performs adequately with large numbers."""
    large_numbers = [10**10] * 6
    start_time = time.time()
    result = multiply_six(large_numbers)
    execution_time = time.time() - start_time
    
    assert execution_time < 0.001  # Should complete in <1ms
    assert result == 10**60
```

## 🔄 Maintenance & Evolution

### Regular Review Schedule
- **Monthly**: Review test coverage and identify gaps
- **Quarterly**: Evaluate testing tools and practices
- **Per Release**: Update performance benchmarks
- **Annual**: Review and update this strategy document

### Metrics to Track
- Test execution time trends
- Coverage percentage over time
- Number of flaky tests
- Test maintenance burden (lines of test code vs. source code)

### Decision Review Process
When changing testing strategy:
1. Document the proposed change and rationale
2. Assess impact on existing tests and CI/CD
3. Update this document with new decisions
4. Communicate changes to all contributors
5. Implement changes incrementally

## ⚠️ Consequences of Non-Compliance

### For Human Developers
- Pull requests will be rejected if tests are missing
- Coverage drops will block merges
- Flaky tests must be fixed immediately

### For AI Agents
- MUST NOT commit code without corresponding tests
- MUST verify all quality gates pass before completing tasks
- MUST update documentation when making testing-related changes
- MUST explain testing decisions in commit messages

## 🎯 Success Metrics

### Short-term Goals (1-3 months)
- [ ] Achieve 90% test coverage
- [ ] Implement CI/CD pipeline
- [ ] Zero flaky tests
- [ ] Test suite runs in <30 seconds

### Long-term Goals (6-12 months)
- [ ] 95% test coverage maintained
- [ ] Property-based testing for all mathematical functions
- [ ] Performance regression testing
- [ ] Automated security testing

---

**Document Version**: 1.0  
**Last Updated**: 2024-10-11  
**Next Review**: 2024-11-11  
**Owner**: Development Team  
**Approved By**: [To be filled]

---

*This document is a living standard. All changes must be reviewed and approved by the development team.*