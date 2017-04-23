import os
import csv

from expectedPoints import summariseGame
from expectedPoints.utility import add_dicts


def cycle_files(folder):
    values = {"off": {}, "def": {}}
    number_of = {"off": {}, "def": {}}
    count_files = 0
    for filename in os.listdir(folder):

        if "csv" not in filename:
            count_files += 1
            with open(folder + "//" + filename, "r") as file:
                game_text = file.read()
            value_game = summariseGame.summarise_game(game_text)
            values["off"] = add_dicts(values["off"], value_game["values"]["off"])
            values["def"] = add_dicts(values["def"], value_game["values"]["def"])
            number_of["off"] = add_dicts(number_of["off"], value_game["number_of"]["off"])
            number_of["def"] = add_dicts(number_of["def"], value_game["number_of"]["def"])
    with open(folder + '//values.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in values["off"].items():
            writer.writerow([key, value])
    with open(folder + '//number_of.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in number_of["off"].items():
            writer.writerow([key, value])
    print(count_files)
    return {"values": values, "number_of": number_of}

beta = cycle_files("C://Users//Mark//PycharmProjects//pointsEstimationFolder//BaseAttempt")
print(beta["values"]["off"])
print(beta["number_of"]["off"])
# Last round done, ASE season 23 II.1
# Round 2