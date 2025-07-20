from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum
from datetime import datetime
import logging
import json
import os

class LogLevel(Enum):
    """Enum for logging levels."""
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

@dataclass
class LogMessage:
    """Dataclass for log messages."""
    timestamp: datetime
    level: LogLevel
    message: str

class Logger:
    """Logger class."""
    def __init__(self, log_level: LogLevel = LogLevel.INFO):
        """Initialize the logger.

        Args:
            log_level (LogLevel, optional): The logging level. Defaults to LogLevel.INFO.
        """
        self.log_level = log_level
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.log_level.value)
        self.handler = logging.StreamHandler()
        self.handler.setLevel(self.log_level.value)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)

    def debug(self, message: str) -> None:
        """Log a debug message.

        Args:
            message (str): The message to log.
        """
        if self.log_level.value <= logging.DEBUG:
            self.logger.debug(message)

    def info(self, message: str) -> None:
        """Log an info message.

        Args:
            message (str): The message to log.
        """
        if self.log_level.value <= logging.INFO:
            self.logger.info(message)

    def warning(self, message: str) -> None:
        """Log a warning message.

        Args:
            message (str): The message to log.
        """
        if self.log_level.value <= logging.WARNING:
            self.logger.warning(message)

    def error(self, message: str) -> None:
        """Log an error message.

        Args:
            message (str): The message to log.
        """
        if self.log_level.value <= logging.ERROR:
            self.logger.error(message)

    def critical(self, message: str) -> None:
        """Log a critical message.

        Args:
            message (str): The message to log.
        """
        if self.log_level.value <= logging.CRITICAL:
            self.logger.critical(message)

def load_config(config_file: str) -> Dict[str, str]:
    """Load the configuration from a file.

    Args:
        config_file (str): The path to the configuration file.

    Returns:
        Dict[str, str]: The loaded configuration.
    """
    try:
        with open(config_file, 'r') as file:
            config = json.load(file)
            return config
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse configuration file: {e}")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Configuration file not found: {e}")

def main():
    """Main function."""
    logger = Logger(LogLevel.INFO)
    config = load_config('config.json')
    logger.info(f"Loaded configuration: {config}")

if __name__ == "__main__":
    main()