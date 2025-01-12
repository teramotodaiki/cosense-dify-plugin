# Cosense Dify Plugin Tests

This directory contains tests for the Cosense Dify Plugin.

## Structure

- `plugin/` - Tests for plugin functionality
  - `test_imports.py` - Verify plugin imports and basic functionality
- `conftest.py` - Pytest configuration and fixtures

## Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/plugin/test_imports.py
```

## Adding New Tests

1. Create test files in the appropriate subdirectory
2. Use pytest fixtures from conftest.py where needed
3. Follow the existing test patterns
