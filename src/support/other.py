import os
import random
import string
from tkinter import messagebox
from typing import Any

import requests
from requests import RequestException

from src.settings import TMP
from src.support.my_iter import MyIter
from ui.web_view.base import View


def batched(lst: list, batch_size: int) -> list[list]:
    return [lst[i: i + batch_size] for i in range(0, len(lst), batch_size)]


def is_int(value: Any) -> bool:
    try:
        return isinstance(int(value), int)
    except ValueError:
        return False


class Json:
    import json as __json

    def __init__(self, json_str: str | None = None, **json_dict_or_list) -> None:
        if json_dict_or_list is None:
            json_dict_or_list = {}

        self.json_dict_or_list: dict = json_dict_or_list
        self.json_str: str | None = json_str

    def loads(self, json_str: str | None = None) -> dict:
        """Convert a JSON string to a dictionary or a list.

        Parameters
        ----------
            json_str (str, optional): The JSON string to be converted. If not provided,
                the function will use the `json_str` attribute of the instance. Defaults to None.

        Returns
        -------
            None | dict[str] | list[any]: The converted dictionary or list. If the conversion
                fails, an empty dictionary is returned.

        """
        json_str = json_str or self.json_str

        if json_str is not None:
            try:
                self.json_dict_or_list = self.__json.loads(json_str)
            except self.__json.JSONDecodeError:
                self.json_dict_or_list = {}

        return self.json_dict_or_list

    def dumps(self, json_dict: dict | list | None = None) -> str:
        """Converts a dictionary or list to a JSON string representation.

        Args:
        ----
            json_dict (dict | list, optional): The dictionary or list to convert to a JSON string. Defaults to None.

        Returns:
        -------
            str: The JSON string representation of the input.

        """
        json_dict = json_dict or self.json_dict_or_list

        if json_dict is not None:
            try:
                self.json_str = self.__json.dumps(json_dict)
            except self.__json.JSONDecodeError:
                self.json_str = ""

        return self.json_str

    def items(self):  # noqa: ANN201
        """Return a list of key-value pairs from the JSON dictionary or list.

        Returns
        -------
            list: A list of tuples representing the key-value pairs from the JSON dictionary or list.
                  If the JSON is empty or not a dictionary, an empty list is returned.
        """
        if isinstance(self.json_dict_or_list, dict) and self.json_dict_or_list:
            return list(self.json_dict_or_list.items())
        return []

    def keys(self):  # noqa: ANN201
        """Returns a list of keys in the json_dict_or_list attribute.

        :return: A list of keys in the json_dict_or_list attribute.
        :rtype: list
        """
        if isinstance(self.json_dict_or_list, dict) and self.json_dict_or_list:
            return list(self.json_dict_or_list.keys())
        return []

    def values(self):  # noqa: ANN201
        """Return the values of the JSON dictionary or list.

        :return: A list of values from the JSON dictionary or list.
        :rtype: list
        """
        if isinstance(self.json_dict_or_list, dict) and self.json_dict_or_list:
            return list(self.json_dict_or_list.values())
        return []

    def get(  # noqa: ANN201
            self, __key: int | str | tuple, default: Any = None,  # noqa: ANN401
    ):
        if isinstance(self.json_dict_or_list, dict):
            return self.json_dict_or_list.get(__key, default)

    def __str__(self) -> str:
        """Return the values of the JSON dictionary or list.

        :return: A list of values from the JSON dictionary or list.
        :rtype: list
        """
        return self.json_str or f"json string = {self.json_str}" \
                                f" dict_or_list = {self.json_dict_or_list}"

    def __getitem__(self, key: str):  # noqa: ANN201
        """Get the item with the specified value from the JSON dictionary or list.

        Parameters
        ----------
            value (Any): The value to search for in the JSON dictionary or list.

        Returns
        -------
            Any: The item with the specified value if found, otherwise None.
        """
        return self.json_dict_or_list.get(key)

    def __setitem__(self, key, value) -> None:  # noqa: ANN201 ANN001
        self.json_dict_or_list[key] = value

    def __iter__(self):  # noqa: ANN201
        """Iterates over the `json_dict_or_list` attribute and yields each item.

        Yields
        ------
            str | int | tuple: The items in the `json_dict_or_list` attribute.
        """
        yield from self.json_dict_or_list


class Translate:
    def __init__(self, config: dict) -> None:
        self.config = config

    def get_translate_item(self, item: str) -> str:
        return self.config["translation"].get(item, 'Не выбран урок')

    def get_translate_book(self, item: str, book_name: str, class_: int | str, oge: bool = False) -> str:
        item = self.get_translate_item(item)
        return (
            self.config["oge"][item][book_name]["file"]
            if oge
            else self.config["classes"][f"{class_}"][
                item
            ][book_name]["file"]
        )


def web_view(self: object, urls: MyIter) -> None:
    url: str = urls()
    if url.endswith(".mp4"):
        install_and_open_video(url)
    else:
        view = "".join(random.sample(string.ascii_letters, 20))
        setattr(self, view, View(url))
        getattr(self, view).show()


def install_and_open_video(url: str) -> None:
    try:
        response = requests.get(url)
        response.raise_for_status()
        path_to_video = os.path.join(TMP, f"{''.join(random.sample(string.ascii_letters, 20))}.mp4")
        with open(path_to_video, "wb") as file:
            file.write(response.content)

        os.startfile(path_to_video)

    except RequestException as e:
        messagebox.showerror("Error", f"Не получилось загрузить видео {e}")
