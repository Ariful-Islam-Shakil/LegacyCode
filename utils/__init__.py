import os
import sys
import logging
import json
from typing import Dict, List, Optional
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_config(config_file: Path) -> Dict[str, str]:
    """
    Load configuration from a JSON file.

    Args:
        config_file (Path): Path to the configuration file.

    Returns:
        Dict[str, str]: Configuration dictionary.

    Raises:
        FileNotFoundError: If the configuration file does not exist.
        json.JSONDecodeError: If the configuration file is not valid JSON.
    """
    try:
        with config_file.open('r') as f:
            return json.load(f)
    except FileNotFoundError as e:
        logger.error(f"Configuration file not found: {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in configuration file: {e}")
        sys.exit(1)

def get_config(config_file: Path) -> Dict[str, str]:
    """
    Get the configuration from the specified file.

    Args:
        config_file (Path): Path to the configuration file.

    Returns:
        Dict[str, str]: Configuration dictionary.
    """
    return load_config(config_file)

def main() -> None:
    """
    Main entry point of the script.
    """
    config_file = Path('config.json')
    config = get_config(config_file)
    logger.info(f"Loaded configuration: {config}")

if __name__ == '__main__':
    main()