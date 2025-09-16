""" Player models located here lol """

from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name: str, score: int, role:str):
        self.name = name
        self.score = score
        self.role = role


    @abstractmethod
    def move():
        pass


class Human(Player):
    def __init__(self, name, score, role):
        super().__init__(name, score, role)

    def move():
        pass


class Bot(Player):
    def __init__(self, name, score, role):
        super().__init__(name, score, role)

    def move():
        pass