import os
import sys
import pathlib
import logging
import typing as t

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

def get_current_directory() -> pathlib.Path:
    """
    Returns the current working directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The current working directory.

    Raises:
        None
    """
    return pathlib.Path(os.getcwd())

def get_parent_directory(path: pathlib.Path) -> pathlib.Path:
    """
    Returns the parent directory of the given path as a pathlib.Path object.

    Args:
        path (pathlib.Path): The path to get the parent directory for.

    Returns:
        pathlib.Path: The parent directory of the given path.

    Raises:
        TypeError: If the path is not a pathlib.Path object.
    """
    if not isinstance(path, pathlib.Path):
        raise TypeError("The path must be a pathlib.Path object.")
    return path.parent

def get_project_root() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_parent_directory(get_current_directory())

def get_project_root_dir() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root())

def get_project_root_path() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root()

def get_project_root_dir_path() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root()

def get_project_root_dir_path_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir())

def get_project_root_dir_path_pathlib() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path()

def get_project_root_dir_path_pathlib_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib())

def get_project_root_dir_path_pathlib_path() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib()

def get_project_root_dir_path_pathlib_path_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path())

def get_project_root_dir_path_pathlib_path_pathlib() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib_path()

def get_project_root_dir_path_pathlib_path_pathlib_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path_pathlib())

def get_project_root_dir_path_pathlib_path_pathlib_path() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib_path_pathlib()

def get_project_root_dir_path_pathlib_path_pathlib_path_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path_pathlib_path())

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib_path_pathlib_path()

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path_pathlib_path_pathlib())

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib_path_pathlib_path_pathlib()

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path())

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path()

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib())

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib()

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path())

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path()

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib())

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib()

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path())

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path()

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib())

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib()

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path())

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path()

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib())

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib()

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path())

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path()

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib())

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib()

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path())

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path()

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib())

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib()

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path())

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path()

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib())

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path() -> pathlib.Path:
    """
    Returns the project root directory as a pathlib.Path object.

    Args:
        None

    Returns:
        pathlib.Path: The project root directory.

    Raises:
        None
    """
    return get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib()

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_str() -> str:
    """
    Returns the project root directory as a string.

    Args:
        None

    Returns:
        str: The project root directory.

    Raises:
        None
    """
    return str(get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path_pathlib_path())

def get_project_root_dir_path_pathlib_path_pathlib_path_pathlib_path_path