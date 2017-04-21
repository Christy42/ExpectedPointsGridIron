import os

from expectedPoints import summariseGame
from expectedPoints.utility import add_dicts


def cycle_files(folder):
    values = {}
    number_of = {}
    for filename in os.listdir(folder):
        with open(filename, "w") as file:
            game_text = file.read()
        value_game = summariseGame.summarise_game(game_text)
        values = add_dicts(values, value_game["values"])
        number_of = add_dicts(number_of, value_game["number_of"])
    return {"values": values, "number_of": number_of}