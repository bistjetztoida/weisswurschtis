# API Reference

## Main Module

### `main(args: Optional[list] = None) -> int`

Main entry point for the application.

**Parameters:**
- `args` (Optional[list]): Command-line arguments (defaults to sys.argv[1:])

**Returns:**
- int: Exit code (0 for success, non-zero for failure)

**Example:**
```python
from weisswurschtis.main import main

# Run with default arguments
exit_code = main()

# Run with custom arguments
exit_code = main(['--help'])
```

## Config Module

### `Config` (dataclass)

Application configuration.

**Attributes:**
- `debug` (bool): Enable debug mode (default: False)
- `log_level` (str): Logging level (default: "INFO")
- `data_dir` (Optional[Path]): Data directory path

**Methods:**
- `__post_init__()`: Validates configuration and creates data directory if needed

### `load_config(config_file: Optional[Path] = None) -> Config`

Load configuration from file or use defaults.

**Parameters:**
- `config_file` (Optional[Path]): Path to configuration file

**Returns:**
- Config: Configuration object

## Utils Module

### `example_function(value: int) -> int`

Example utility function.

**Parameters:**
- `value` (int): An integer value

**Returns:**
- int: The value incremented by one

**Example:**
```python
from weisswurschtis.utils import example_function

result = example_function(5)  # Returns 6
```

### `process_items(items: List[Any]) -> List[Any]`

Process a list of items, filtering out None values.

**Parameters:**
- `items` (List[Any]): List of items to process

**Returns:**
- List[Any]: Processed list of items

**Example:**
```python
from weisswurschtis.utils import process_items

result = process_items([1, None, 3])  # Returns [1, 3]
```
