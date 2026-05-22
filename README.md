# weisswurschtis 🥰

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A modern, production-ready Python project template with best practices, comprehensive testing, and professional tooling.

## ✨ Features

- ✅ **Modern Python Packaging** - `pyproject.toml` based configuration
- ✅ **Comprehensive Testing** - pytest with coverage reporting
- ✅ **Code Quality** - black, isort, pylint, mypy for code standards
- ✅ **Pre-commit Hooks** - Automatic formatting on commit
- ✅ **Type Hints** - Full static typing throughout codebase
- ✅ **CI/CD Ready** - GitHub Actions workflows included
- ✅ **Professional Logging** - Structured logging setup
- ✅ **Configuration Management** - JSON-based config loading
- ✅ **Utilities** - Retry decorator, batching, and more
- ✅ **Documentation** - Comprehensive docs and API reference
- ✅ **Python 3.8+** - Support for multiple Python versions

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/bistjetztoida/weisswurschtis.git
cd weisswurschtis

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install
```

### Running the Application

```bash
# Run with default settings
python -m weisswurschtis

# Run with debug logging
python -m weisswurschtis --debug

# Run with custom config
python -m weisswurschtis --config config.json

# Show help
python -m weisswurschtis --help
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_utils.py -v

# Run with markers
pytest -m "not slow"
```

## 🛠️ Development

### Code Formatting

```bash
# Format code with black
black src/ tests/

# Sort imports with isort
isort src/ tests/

# Check types with mypy
mypy src/

# Lint with pylint
pylint src/
```

### Project Structure

```
weisswurschtis/
├── src/weisswurschtis/          # Main package
│   ├── __init__.py              # Package initialization
│   ├── main.py                  # Entry point with CLI
│   ├── config.py                # Configuration management
│   └── utils.py                 # Utility functions
├── tests/                        # Test suite
│   ├── __init__.py
│   ├── test_main.py             # Main module tests
│   └── test_utils.py            # Utility function tests
├── docs/                         # Documentation
│   ├── index.md                 # Documentation index
│   └── api.md                   # API reference
├── .github/
│   ├── workflows/               # GitHub Actions workflows
│   └── ISSUE_TEMPLATE/          # Issue templates
├── .pre-commit-config.yaml      # Pre-commit hooks config
├── .gitignore                   # Git ignore rules
├── pyproject.toml               # Modern Python packaging
├── setup.py                     # Legacy packaging support
├── pytest.ini                   # Pytest configuration
├── requirements.txt             # Production dependencies
├── requirements-dev.txt         # Development dependencies
├── LICENSE                      # MIT License
└── README.md                    # This file
```

## 📦 Dependencies

### Production
None (minimal dependencies by design)

### Development
- pytest - Testing framework
- pytest-cov - Coverage reporting
- black - Code formatter
- isort - Import sorter
- pylint - Linter
- mypy - Type checker
- pre-commit - Git hooks

## 📚 API Reference

See [docs/api.md](docs/api.md) for detailed API documentation.

### Core Modules

#### `main`
Entry point with CLI argument parsing and logging setup.

```python
from weisswurschtis import main

exit_code = main()
```

#### `config`
Configuration management with JSON support.

```python
from weisswurschtis.config import Config, load_config

config = load_config('config.json')
```

#### `utils`
Utility functions including retry decorator and batching.

```python
from weisswurschtis.utils import retry, batched

@retry(max_attempts=3, delay=1.0)
def my_function():
    pass
```

## 🔄 CI/CD

GitHub Actions workflow runs automatically on:
- Push to main/develop branches
- Pull requests

Tests matrix includes Python 3.8, 3.9, 3.10, 3.11.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**bistjetztoida** - [GitHub](https://github.com/bistjetztoida)

## 🙏 Acknowledgments

- Built with Python best practices
- Inspired by professional Python projects
- Community-driven development

---

**Made with ❤️ for the Python community**
