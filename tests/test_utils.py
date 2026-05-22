"""Tests for utility functions."""

import pytest
from weisswurschtis.utils import example_function, process_items


class TestExampleFunction:
    """Test cases for example_function."""

    def test_example_function_basic(self) -> None:
        """Test example_function with basic input."""
        assert example_function(5) == 6

    def test_example_function_zero(self) -> None:
        """Test example_function with zero."""
        assert example_function(0) == 1

    def test_example_function_negative(self) -> None:
        """Test example_function with negative input."""
        assert example_function(-1) == 0


class TestProcessItems:
    """Test cases for process_items."""

    def test_process_items_basic(self) -> None:
        """Test process_items with basic list."""
        result = process_items([1, 2, 3])
        assert result == [1, 2, 3]

    def test_process_items_with_none(self) -> None:
        """Test process_items filters out None values."""
        result = process_items([1, None, 3])
        assert result == [1, 3]

    def test_process_items_empty(self) -> None:
        """Test process_items with empty list."""
        result = process_items([])
        assert result == []


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
