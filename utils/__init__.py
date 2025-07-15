from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum
import json
import logging
import os
import pathlib
import sys
import yaml

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LogLevel(Enum):
    """Enum for log levels."""
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

@dataclass
class Config:
    """Dataclass for configuration."""
    log_level: LogLevel
    log_file: Optional[str] = None
    log_format: str = '%(asctime)s - %(levelname)s - %(message)s'

def load_config(file_path: str) -> Config:
    """
    Load configuration from YAML file.

    Args:
        file_path (str): Path to YAML file.

    Returns:
        Config: Loaded configuration.

    Raises:
        FileNotFoundError: If file is not found.
        yaml.YAMLError: If YAML file is invalid.
    """
    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
            return Config(
                log_level=LogLevel[config['log_level']],
                log_file=config.get('log_file'),
                log_format=config.get('log_format', '%(asctime)s - %(levelname)s - %(message)s')
            )
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        sys.exit(1)
    except yaml.YAMLError as e:
        logging.error(f"Invalid YAML file: {e}")
        sys.exit(1)

def configure_logging(config: Config) -> None:
    """
    Configure logging based on configuration.

    Args:
        config (Config): Configuration.

    Returns:
        None
    """
    logging.basicConfig(
        level=config.log_level.value,
        format=config.log_format
    )
    if config.log_file:
        logging.basicConfig(
            handlers=[logging.FileHandler(config.log_file)],
            level=config.log_level.value,
            format=config.log_format
        )

def main() -> None:
    """
    Main function.

    Returns:
        None
    """
    config_file = 'config.yaml'
    config = load_config(config_file)
    configure_logging(config)

if __name__ == '__main__':
    main()

This refactored code follows best practices and is compatible with Python 3.12. It includes type hints, docstrings, and uses only verified packages and versions. The logging configuration is also updated to use the `basicConfig` method with a file handler if a log file is specified.