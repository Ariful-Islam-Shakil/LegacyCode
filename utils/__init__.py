from typing import List, Dict, Optional
import json
import logging
import os

class Config:
    """Configuration class for the application.

    Attributes:
        config_file (str): Path to the configuration file.
        config (Dict[str, str]): Loaded configuration.
    """

    def __init__(self, config_file: str = "config.json"):
        """Initialize the configuration class.

        Args:
            config_file (str, optional): Path to the configuration file. Defaults to "config.json".
        """
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self) -> Dict[str, str]:
        """Load the configuration from the file.

        Returns:
            Dict[str, str]: Loaded configuration.
        """
        try:
            with open(self.config_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            logging.error(f"Configuration file '{self.config_file}' not found.")
            raise
        except json.JSONDecodeError:
            logging.error(f"Invalid configuration file '{self.config_file}'.")
            raise

    def save_config(self, config: Dict[str, str]) -> None:
        """Save the configuration to the file.

        Args:
            config (Dict[str, str]): Configuration to save.
        """
        try:
            with open(self.config_file, "w") as file:
                json.dump(config, file, indent=4)
        except Exception as e:
            logging.error(f"Failed to save configuration: {e}")

class Application:
    """Application class.

    Attributes:
        config (Config): Configuration instance.
    """

    def __init__(self, config: Config):
        """Initialize the application.

        Args:
            config (Config): Configuration instance.
        """
        self.config = config

    def run(self) -> None:
        """Run the application."""
        print("Application started.")
        print("Configuration:")
        for key, value in self.config.config.items():
            print(f"{key}: {value}")

def main() -> None:
    """Main function."""
    logging.basicConfig(level=logging.INFO)
    config = Config()
    app = Application(config)
    app.run()

if __name__ == "__main__":
    main()

This refactored code follows best practices and is fully compatible with Python 3.12. It includes clean and correct Python docstrings following the Google Python style guide. The code uses only packages and versions that are verified to work with Python 3.12.