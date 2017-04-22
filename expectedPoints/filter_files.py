import os

from expectedPoints import summariseGame
from expectedPoints.utility import add_dicts


def cycle_files(folder):
    values = {"off": {}, "def": {}}
    number_of = {"off": {}, "def": {}}
    for filename in os.listdir(folder):
        with open(folder + "//" + filename, "r") as file:
            game_text = file.read()
        value_game = summariseGame.summarise_game(game_text)
        values["off"] = add_dicts(values["off"], value_game["values"]["off"])
        values["def"] = add_dicts(values["def"], value_game["values"]["def"])
        number_of["off"] = add_dicts(number_of["off"], value_game["number_of"]["off"])
        number_of["def"] = add_dicts(number_of["def"], value_game["number_of"]["def"])
    return {"values": values, "number_of": number_of}

beta = cycle_files("C://Users//Mark//PycharmProjects//pointsEstimationFolder//BaseAttempt")
print(beta["values"]["off"])
print(beta["number_of"]["off"])
