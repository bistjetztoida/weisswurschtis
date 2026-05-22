"""Tests for main module."""

import pytest
from weisswurschtis.main import main


class TestMain:
    """Test cases for main function."""

    def test_main_exits_successfully(self) -> None:
        """Test main function exits with code 0."""
        exit_code = main([])
        assert exit_code == 0

    def test_main_with_help(self) -> None:
        """Test main function with help argument."""
        with pytest.raises(SystemExit) as exc_info:
            main(["--help"])
        assert exc_info.value.code == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
