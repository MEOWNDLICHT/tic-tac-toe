""" Handles the serialization and deserialization of scores into json """

import json


class Scores:
    def __init__(self, file='score.json'):
        with open(file, 'r') as f:
            self.data = json.load(f)