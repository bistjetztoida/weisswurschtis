"""Main entry point for weisswurschtis application."""

import argparse
import logging
import sys
from pathlib import Path
from typing import Optional

from .config import Config, load_config

# Configure logging
logger = logging.getLogger(__name__)


def setup_logging(debug: bool = False) -> None:
    """Configure logging for the application.
    
    Args:
        debug: Enable debug-level logging if True
    """
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def create_parser() -> argparse.ArgumentParser:
    """Create and configure argument parser.
    
    Returns:
        Configured ArgumentParser instance
    """
    parser = argparse.ArgumentParser(
        description='weisswurschtis - A modular Python project',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m weisswurschtis
  python -m weisswurschtis --debug
  python -m weisswurschtis --config config.json
        """
    )
    
    parser.add_argument(
        '--config',
        type=Path,
        default=None,
        help='Path to configuration file'
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug logging'
    )
    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 0.1.0'
    )
    
    return parser


def main(args: Optional[list] = None) -> int:
    """Main entry point for the application.
    
    Args:
        args: Optional list of command-line arguments
        
    Returns:
        Exit code (0 for success, non-zero for failure)
        
    Example:
        >>> exit_code = main()
        >>> sys.exit(exit_code)
    """
    # Parse arguments
    parser = create_parser()
    parsed_args = parser.parse_args(args)
    
    # Setup logging
    setup_logging(parsed_args.debug)
    logger.debug(f"Starting weisswurschtis with args: {parsed_args}")
    
    try:
        # Load configuration
        config = load_config(parsed_args.config)
        logger.info(f"Configuration loaded: debug={config.debug}")
        
        # Ensure data directory exists
        if config.data_dir:
            config.data_dir.mkdir(parents=True, exist_ok=True)
            logger.info(f"Data directory ready: {config.data_dir}")
        
        # Application logic here
        logger.info("Application running successfully")
        return 0
        
    except Exception as e:
        logger.exception(f"Application error: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
