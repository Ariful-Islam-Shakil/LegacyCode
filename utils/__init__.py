from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime
import json
import logging
import os
import sys

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class Config:
    """Configuration class."""
    api_key: str
    api_secret: str
    api_base_url: str
    api_version: str

class API:
    """API class."""
    def __init__(self, config: Config):
        """Initialize the API object.

        Args:
            config (Config): Configuration object.

        Returns:
            None
        """
        self.config = config

    def get_data(self, endpoint: str) -> Optional[Dict]:
        """Get data from the API.

        Args:
            endpoint (str): API endpoint.

        Returns:
            Optional[Dict]: API response data or None if failed.
        """
        try:
            response = self._make_request(endpoint)
            return response.json()
        except Exception as e:
            logging.error(f"Failed to get data: {e}")
            return None

    def _make_request(self, endpoint: str) -> object:
        """Make a request to the API.

        Args:
            endpoint (str): API endpoint.

        Returns:
            object: API response object.
        """
        try:
            url = f"{self.config.api_base_url}{endpoint}{self.config.api_version}"
            headers = {"Authorization": f"Bearer {self.config.api_key}"}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logging.error(f"Failed to make request: {e}")
            raise

def load_config() -> Config:
    """Load configuration from file.

    Returns:
        Config: Configuration object.
    """
    try:
        with open("config.json", "r") as f:
            config_data = json.load(f)
            return Config(**config_data)
    except FileNotFoundError:
        logging.error("Config file not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse config file: {e}")
        sys.exit(1)

def main():
    """Main function."""
    config = load_config()
    api = API(config)
    data = api.get_data("/endpoint")
    if data is not None:
        print(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()

# Third-party package imports
import requests

# Update to the latest version of the requests package
requests.__version__  # Should be 2.33.0 or higher

# Python version check
import sys
if sys.version_info < (3, 12):
    raise RuntimeError("This script requires Python 3.12 or higher.")