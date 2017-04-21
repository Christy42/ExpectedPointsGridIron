from expectedPoints.utility import sum_list, figure_play_fact, calc_next_score


def summarise_game(game):
    """
    :type game: str
    :return:
    """
    quarters = game.split("quarter-")
    play = [quarters[j].split(":") for j in range(1, len(quarters))]
    quarters = [[play[j][i-1][-2:] + ":" + play[j][i][:-2] for i in range(1, len(play[j]))] for j in range(len(play))]

    cut_string = [[quarters[j][i] if int(quarters[j][i][:2]) > 4 or j in [0, 2] else "" for i in range(len(quarters))]
                  for j in range(len(quarters))]
    cut_string = [[cut_string[j][i][5:] for i in range(len(cut_string))] for j in range(len(cut_string))]
    cut_string = [[cut_string[j][i] for i in range(len(cut_string[j])) if cut_string[j][i] != ""]
                  for j in range(len(cut_string))]
    cut_string = [[cut_string[j][i].replace("1st", "spl£S1st").replace("2nd", "spl£S2nd").replace("3rd", "spl£S3rd").
                  replace("4th", "spl£S4th").split("spl£S")[1:] for i in range(len(cut_string[j]))]
                  for j in range(len(cut_string))]

    holder = [[], []]
    holder[0] = sum_list([sum_list(x) for x in cut_string][0:2])
    holder[1] = sum_list([sum_list(x) for x in cut_string][2:4])
    cut_string = holder

    cut_string = [[cut_string[j][i][:4] + "0" + cut_string[j][i][4:] if cut_string[j][i][5] == "-" else cut_string[j][i]
                   for i in range(len(cut_string[j]))] for j in range(2)]

    cut_string = [[cut_string[j][i].replace("Punt", "4th" + figure_play_fact(cut_string[j][i])).
                  replace("Field goal", "4th" + figure_play_fact(cut_string[j][i]))
                   for i in range(len(cut_string[j]))] for j in range(2)]

    cut_string = [[cut_string[j][i].replace("1st", "spl£S1st").replace("2nd", "spl£S2nd").replace("3rd", "spl£S3rd").
                  replace("4th", "spl£S4th").split("spl£S") for i in range(len(cut_string[j]))] for j in range(2)]
    cut_string = [sum_list(half) for half in cut_string]

    cut_string = [[x for x in cut_string[j] if x != ""] for j in range(2)]

    values = {"off": {}, "def": {}}
    number_of = {"off": {}, "def": {}}

    for j in range(2):
        for i in range(len(cut_string[j])):
            score = str(7 * ("TOUCHDOWN" in cut_string[j][i]) + 3 * ("field goal is GOOD" in cut_string[j][i]))

            cut_string[j][i] = cut_string[j][i][:7] + cut_string[j][i][10:12] + "   " + score + "  " + \
            cut_string[j][i][7:10]
    for j in range(2):
        for i in range(len(cut_string[j])):
            score = calc_next_score(cut_string[j], i)

            if cut_string[j][i][:9] in values["off"].keys():
                number_of["def"][cut_string[j][i][:9]] += 1
                number_of["off"][cut_string[j][i][:9]] += 1
                values["def"][cut_string[j][i][:9]] -= score
                values["off"][cut_string[j][i][:9]] += score
            else:
                number_of["off"][cut_string[j][i][:9]] = 1
                number_of["def"][cut_string[j][i][:9]] = 1
                values["def"][cut_string[j][i][:9]] = -score
                values["off"][cut_string[j][i][:9]] = score

    return {"number_of": number_of, "values": values}
