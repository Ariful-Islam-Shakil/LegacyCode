from typing import Dict, List, Optional
import os
import sys
import logging
from pathlib import Path
import json
import yaml

class Config:
    """Configuration class to load and store configuration data.

    Attributes:
        config_file (str): Path to the configuration file.
        config_data (Dict): Loaded configuration data.
    """

    def __init__(self, config_file: str):
        """Initialize the Config class.

        Args:
            config_file (str): Path to the configuration file.

        Raises:
            FileNotFoundError: If the configuration file does not exist.
            json.JSONDecodeError: If the configuration file is not a valid JSON file.
            yaml.YAMLError: If the configuration file is not a valid YAML file.
        """
        self.config_file = config_file
        self.config_data: Optional[Dict] = None

        if not Path(config_file).exists():
            raise FileNotFoundError(f"Configuration file '{config_file}' not found.")

        try:
            with open(config_file, 'r') as file:
                if config_file.endswith('.json'):
                    self.config_data = json.load(file)
                elif config_file.endswith('.yaml') or config_file.endswith('.yml'):
                    self.config_data = yaml.safe_load(file)
                else:
                    raise ValueError(f"Unsupported configuration file format: '{config_file}'")
        except (json.JSONDecodeError, yaml.YAMLError) as e:
            raise ValueError(f"Failed to parse configuration file: {e}")

    def get_config(self) -> Dict:
        """Get the loaded configuration data.

        Returns:
            Dict: Loaded configuration data.
        """
        return self.config_data

def load_config(config_file: str) -> Config:
    """Load configuration data from a file.

    Args:
        config_file (str): Path to the configuration file.

    Returns:
        Config: Loaded configuration data.

    Raises:
        FileNotFoundError: If the configuration file does not exist.
        ValueError: If the configuration file is not a valid JSON or YAML file.
    """
    return Config(config_file)

def main():
    """Main function to test the Config class."""
    config_file = 'config.json'
    config = load_config(config_file)
    config_data = config.get_config()
    print(config_data)

if __name__ == '__main__':
    main()

This refactored code is compatible with Python 3.12 and follows best practices. It uses type hints, Python docstrings, and compatible third-party packages. The code is also well-structured and readable.