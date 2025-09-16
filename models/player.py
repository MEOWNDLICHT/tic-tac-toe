""" Player models located here lol """

from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    @abstractmethod
    def move():
        pass


class Human(Player):
    def __init__(self, name, score):
        super().__init__(name, score)

    def move():
        pass


class Bot(Player):
    def __init__(self, name, score):
        super().__init__(name, score)

    def move():
        pass