def add_dicts(dict_1, dict_2):
    return {element: dict_1.get(element, 0) + dict_2.get(element, 0) for element in set(dict_1) | set(dict_2)}


def sum_list(columns):
    answer = []
    for i in range(len(columns)):
        answer += columns[i]
    return answer


def figure_play_fact(play_line):
    if " incomplete" in play_line or "under pressure from" in play_line:
        return play_line[3:12]
    play_line = play_line.split(" yards")[0]
    negative = -1 if " sacked by " in play_line else 1
    add = 1 * ("-" in play_line[-4:-1])
    dist = int(play_line[-3 - add:-1]) * negative
    place = str((int(play_line[4:6]) - dist) * negative)
    if len(place) == 1:
        place = "0" + place
    field = str(int(play_line[10:12]) + dist)
    if len(field) == 1:
        field = "0" + field
    return "-" + place + play_line[6:10] + field


def calc_next_score(columns, i):
    team = columns[i][-3:]
    for j in range(i, len(columns)):
        if int(columns[j][-6:-5]) > 0:
            return int(columns[j][-6:-5]) * (2 * (team == columns[j][-3:]) - 1)
    return 0
