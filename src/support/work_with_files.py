import os
import random
import string
import zipfile
from collections.abc import Callable
from pathlib import Path

import requests

from src.settings import TMP


class PathToFile:

    def __init__(self, path: str | Path) -> None:
        self.path = path

    def fullpath(self) -> str:
        abspath = os.path.realpath(self.path)
        dir_, name = os.path.dirname(abspath), os.path.basename(abspath)
        return os.path.join(dir_, name)

    def __str__(self) -> str:
        return self.fullpath()


def join_path_to_file(temp_dir: str) -> Callable:
    return lambda file_name: os.path.join(temp_dir, file_name)


def install_and_extract_files(response: requests.Response) -> list[str]:
    """Extracts and opens files from a zip archive.

    Args:
    ----
        response (requests.Response): The response object containing the zip archive.

    Returns:
    -------
        None.
    """
    from src.storage import GlobalStateStorage

    temp_dir = os.path.join(TMP, ''.join(random.sample(string.ascii_letters, 20))) # type: ignore

    zip_file_path = f"{temp_dir}.zip"

    os.makedirs(temp_dir, exist_ok=True)

    with open(zip_file_path, "wb") as file:
        file.write(response.content)
    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        zip_ref.extractall(temp_dir)

    GlobalStateStorage.installed_files.append(zip_file_path)
    GlobalStateStorage.installed_files.extend(list(map(join_path_to_file(temp_dir), os.listdir(temp_dir))))
    return list(map(join_path_to_file(temp_dir), os.listdir(temp_dir)))
