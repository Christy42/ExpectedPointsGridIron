from expectedPoints.utility import sum_list, figure_play_fact, calc_next_score


def get_final_scores(game):
    quarters = game.split("quarter-")
    play = [quarters[j].split(":") for j in range(1, len(quarters))]
    quarters = [[play[j][i-1][-2:] + ":" + play[j][i][:-2] for i in range(1, len(play[j]))] for j in range(len(play))]
    cut_string = [[quarters[j][i] if int(quarters[j][i][:2]) <= 4 and j in [1, 3] else ""
                   for i in range(len(quarters[j]))] for j in range(len(quarters))]

    cut_string = ["".join(x) for x in cut_string]
    cut_string = [x for x in cut_string if x != ""]
    cut_string = [x.replace("1st", "spl£S1st").replace("2nd", "spl£S2nd").replace("3rd", "spl£S3rd")
                   .replace("4th", "spl£S4th").split("spl£S") for x in cut_string]
    value = [{"Team": "DEF", "Score": 0}, {"Team": "DEF", "Score": 0}]
    for i in range(len(cut_string)):
        for j in range(len(cut_string[i])):
            if " TOUCHDOWN!" in cut_string[i][j]:
                value[i]["Score"] = 7
                add = 1 * ("-" == cut_string[i][j][5])
                value[i]["Team"] = cut_string[i][j][7 - add: 10 - add]
                break
            elif "field goal is GOOD" in cut_string[i][j]:
                value[i]["Score"] = 3
                value[i]["Team"] = cut_string[i][j][7 - add: 10 - add]
                break
    return value


def divide_quarters(game):
    quarters = game.split("quarter-")
    play = [quarters[j].split(":") for j in range(1, len(quarters))]
    quarters = [[play[j][i-1][-2:] + ":" + play[j][i][:-2] for i in range(1, len(play[j]))] for j in range(len(play))]

    cut_string = [[quarters[j][i] if int(quarters[j][i][:2]) > 4 or j in [0, 2] else ""
                   for i in range(len(quarters[j]))]
                  for j in range(len(quarters))]

    cut_string = [[cut_string[j][i][5:] for i in range(len(cut_string[j]))] for j in range(len(cut_string))]
    cut_string = [[cut_string[j][i] for i in range(len(cut_string[j])) if cut_string[j][i] != ""]
                  for j in range(len(cut_string))]
    cut_string = [[str(cut_string[j][i]).replace("Gains 1st down!", "XXXXX") for i in range(len(cut_string[j]))]
                  for j in range(len(cut_string))]
    cut_string = [[str(cut_string[j][i]).replace("1st", "spl£S1st").replace("2nd", "spl£S2nd").
                   replace("3rd", "spl£S3rd").replace("4th", "spl£S4th").split("spl£S")[1:]
                   for i in range(len(cut_string[j]))] for j in range(len(cut_string))]

    holder = [[], []]
    holder[0] = sum_list([sum_list(x) for x in cut_string][0:2])
    holder[1] = sum_list([sum_list(x) for x in cut_string][2:4])
    return holder


def handle_fourth_down(segmented_string):
    cut_string = segmented_string

    cut_string = [[cut_string[j][i][:4] + "0" + cut_string[j][i][4:] if cut_string[j][i][5] == "-" else cut_string[j][i]
                   for i in range(len(cut_string[j]))] for j in range(2)]
    cut_string = [[str(cut_string[j][i][:10]) + "0" + str(cut_string[j][i][10:])
                   if str(cut_string[j][i][10]).isnumeric()
                   else cut_string[j][i] for i in range(len(cut_string[j]))] for j in range(2)]
    cut_string = [[str(cut_string[j][i]).replace("Punt", "4th" + figure_play_fact(cut_string[j][i])).
                  replace("Field goal", "4th" + figure_play_fact(cut_string[j][i]))
                   for i in range(len(cut_string[j]))] for j in range(2)]

    cut_string = [[str(cut_string[j][i]).replace("1st", "spl£S1st").replace("2nd", "spl£S2nd").
                   replace("3rd", "spl£S3rd").replace("4th", "spl£S4th").split("spl£S")
                   for i in range(len(cut_string[j]))] for j in range(2)]
    cut_string = [sum_list(half) for half in cut_string]

    cut_string = [[x for x in cut_string[j] if x != ""] for j in range(2)]
    return cut_string


def summarise_game(game):
    """
    :type game: str
    :return:
    """
    cut_string = divide_quarters(game)
    cut_string = handle_fourth_down(cut_string)
    end_scores = get_final_scores(game)
    return assign_weights(cut_string, end_scores)


def assign_weights(segmented_string, end_scores):
    cut_string = list(segmented_string)
    for j in range(2):
        for i in range(len(cut_string[j])):
            score = str(7 * (" TOUCHDOWN!" in cut_string[j][i]) + 3 * ("field goal is GOOD" in cut_string[j][i]))
            cut_string[j][i] = cut_string[j][i][:7] + cut_string[j][i][10:12] + "   " + score + "   " + \
                cut_string[j][i][7:10]
        cut_string[j].append("Default00" + "   " + str(end_scores[j]["Score"]) + "   " + end_scores[j]["Team"])
    values = {"off": {}, "def": {}}
    number_of = {"off": {}, "def": {}}

    for j in range(2):
        for i in range(len(cut_string[j]) - 1):
            score = calc_next_score(cut_string[j], i)
            if not cut_string[j][i][3:9].replace("-", "").isnumeric():
                print(cut_string[j][i])
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
