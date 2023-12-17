import requests


class Book:
    def __init__(self, description: str, file: str, image: str, type_: str, reinforce: bool=False):
        self.description = description
        self.file = file
        self.image = image
        self.type = type_
        self.reinforce = reinforce
        self.__content = {}

    @property
    def content(self):
        if not self.__content:
            self.__content = requests.get()



        return self.__content
