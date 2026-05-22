"""Configuration management for weisswurschtis."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional
import json
import logging

logger = logging.getLogger(__name__)


@dataclass
class Config:
    """Application configuration.
    
    Attributes:
        debug: Enable debug mode
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        data_dir: Directory for application data
    """
    debug: bool = False
    log_level: str = "INFO"
    data_dir: Optional[Path] = field(default=None)
    
    def __post_init__(self) -> None:
        """Validate configuration after initialization."""
        # Convert data_dir to Path if it's a string
        if isinstance(self.data_dir, str):
            self.data_dir = Path(self.data_dir)
        
        # Validate log level
        valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
        if self.log_level not in valid_levels:
            logger.warning(f"Invalid log level '{self.log_level}', using 'INFO'")
            self.log_level = "INFO"
        
        # Create data directory if specified
        if self.data_dir:
            self.data_dir.mkdir(parents=True, exist_ok=True)
            logger.debug(f"Data directory created/verified: {self.data_dir}")


def load_config(config_file: Optional[Path] = None) -> Config:
    """Load configuration from file or use defaults.
    
    Args:
        config_file: Path to JSON configuration file
        
    Returns:
        Config object with loaded settings
        
    Raises:
        FileNotFoundError: If config file is specified but not found
        json.JSONDecodeError: If config file is not valid JSON
    """
    defaults = {
        "debug": False,
        "log_level": "INFO",
        "data_dir": None
    }
    
    if config_file and config_file.exists():
        logger.debug(f"Loading config from {config_file}")
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
            logger.info(f"Config file loaded successfully")
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in config file: {e}")
            raise
        except IOError as e:
            logger.error(f"Failed to read config file: {e}")
            raise
        
        # Merge with defaults
        for key in defaults:
            if key not in config_data:
                config_data[key] = defaults[key]
        
        return Config(**config_data)
    elif config_file:
        raise FileNotFoundError(f"Config file not found: {config_file}")
    
    logger.debug("Using default configuration")
    return Config(**defaults)


def save_config(config: Config, config_file: Path) -> None:
    """Save configuration to file.
    
    Args:
        config: Config object to save
        config_file: Path where to save the configuration
    """
    config_dict = {
        "debug": config.debug,
        "log_level": config.log_level,
        "data_dir": str(config.data_dir) if config.data_dir else None
    }
    
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config_dict, f, indent=2)
    
    logger.info(f"Configuration saved to {config_file}")
