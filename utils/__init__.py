from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LogLevel(str, Enum):
    """Enum representing log levels."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

@dataclass
class Config:
    """Dataclass representing configuration."""
    api_key: str
    api_secret: str
    endpoint: str

def load_config(config_path: Path) -> Config:
    """
    Load configuration from a JSON file.

    Args:
        config_path: Path to the configuration file.

    Returns:
        Config: Loaded configuration.

    Raises:
        FileNotFoundError: If the configuration file is not found.
        json.JSONDecodeError: If the configuration file is not valid JSON.
    """
    try:
        with config_path.open('r') as file:
            config_data = json.load(file)
            return Config(**config_data)
    except FileNotFoundError as e:
        logger.error(f"Configuration file not found: {e}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in configuration file: {e}")
        raise

def get_config() -> Config:
    """
    Get the configuration from the default configuration file.

    Returns:
        Config: Loaded configuration.
    """
    config_path = Path(__file__).parent / 'config.json'
    return load_config(config_path)

def main() -> None:
    """Main function."""
    config = get_config()
    logger.info(f"Loaded configuration: {config}")

if __name__ == "__main__":
    main()