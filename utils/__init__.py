from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum
import json
import logging
from pathlib import Path
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import uuid

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BuildStatus(Enum):
    """Enum for build status."""
    SUCCESS = 0
    FAILURE = 1
    SKIPPED = 2

@dataclass
class BuildResult:
    """Dataclass for build result."""
    status: BuildStatus
    output: str

def get_build_status(output: str) -> BuildStatus:
    """
    Determine the build status based on the output.

    Args:
        output (str): The build output.

    Returns:
        BuildStatus: The build status.

    Raises:
        ValueError: If the output is invalid.
    """
    if re.search(r'Build Succeeded', output):
        return BuildStatus.SUCCESS
    elif re.search(r'Build Failed', output):
        return BuildStatus.FAILURE
    else:
        raise ValueError('Invalid build output')

def run_command(command: str) -> BuildResult:
    """
    Run a command and capture the output.

    Args:
        command (str): The command to run.

    Returns:
        BuildResult: The build result.

    Raises:
        subprocess.CalledProcessError: If the command fails.
    """
    try:
        output = subprocess.check_output(command, shell=True).decode('utf-8')
        status = get_build_status(output)
        return BuildResult(status=status, output=output)
    except subprocess.CalledProcessError as e:
        logging.error(f'Command failed with return code {e.returncode}')
        return BuildResult(status=BuildStatus.FAILURE, output=f'Command failed with return code {e.returncode}')

def build_project(project_path: Path) -> BuildResult:
    """
    Build a project.

    Args:
        project_path (Path): The project path.

    Returns:
        BuildResult: The build result.

    Raises:
        FileNotFoundError: If the project path does not exist.
    """
    if not project_path.exists():
        raise FileNotFoundError(f'Project path {project_path} does not exist')
    command = f'cmake -B {project_path / "build"} -S {project_path}'
    return run_command(command)

def clean_project(project_path: Path) -> None:
    """
    Clean a project.

    Args:
        project_path (Path): The project path.
    """
    if project_path.exists():
        shutil.rmtree(project_path)

def main() -> None:
    """
    Main function.
    """
    project_path = Path(sys.argv[1])
    clean_project(project_path)
    build_result = build_project(project_path)
    logging.info(f'Build result: {build_result.status}')

if __name__ == '__main__':
    main()