from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing_extensions import TypedDict

class LogLevel(str, Enum):
    """Enum representing the log level."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"

@dataclass
class LogMessage:
    """Dataclass representing a log message."""
    timestamp: datetime
    level: LogLevel
    message: str

    def __post_init__(self):
        """Initialize the timestamp."""
        self.timestamp = datetime.now()

class Logger:
    """Logger class."""
    def __init__(self, log_file: Path, log_level: LogLevel = LogLevel.INFO):
        """Initialize the logger.

        Args:
            log_file (Path): The path to the log file.
            log_level (LogLevel, optional): The log level. Defaults to LogLevel.INFO.
        """
        self.log_file = log_file
        self.log_level = log_level
        self.log_messages: List[LogMessage] = []

    def log(self, message: str, level: LogLevel = LogLevel.INFO):
        """Log a message.

        Args:
            message (str): The message to log.
            level (LogLevel, optional): The log level. Defaults to LogLevel.INFO.

        Returns:
            None
        """
        if level >= self.log_level:
            log_message = LogMessage(datetime.now(), level, message)
            self.log_messages.append(log_message)
            self._write_to_log_file(log_message)

    def _write_to_log_file(self, log_message: LogMessage):
        """Write a log message to the log file.

        Args:
            log_message (LogMessage): The log message to write.

        Returns:
            None
        """
        with open(self.log_file, "a") as f:
            f.write(f"{log_message.timestamp} - {log_message.level.value} - {log_message.message}\n")

    def get_log_messages(self) -> List[LogMessage]:
        """Get the log messages.

        Returns:
            List[LogMessage]: The log messages.
        """
        return self.log_messages

class Config(TypedDict):
    """Config dictionary."""
    log_file: str
    log_level: str

def load_config(config_file: Path) -> Config:
    """Load the config from a file.

    Args:
        config_file (Path): The path to the config file.

    Returns:
        Config: The config.
    """
    try:
        with open(config_file, "r") as f:
            config_str = f.read()
            return Config(**config_str)
    except Exception as e:
        raise ValueError("Failed to load config") from e

def main():
    """Main function."""
    config_file = Path("config.json")
    config = load_config(config_file)
    log_file = Path(config["log_file"])
    logger = Logger(log_file, LogLevel[config["log_level"]])

    logger.log("This is a debug message", LogLevel.DEBUG)
    logger.log("This is an info message")
    logger.log("This is a warning message", LogLevel.WARNING)
    logger.log("This is an error message", LogLevel.ERROR)

    log_messages = logger.get_log_messages()
    for log_message in log_messages:
        print(log_message)

if __name__ == "__main__":
    main()