from expectedPoints.utility import add_dicts, calc_next_score, figure_play_fact, sum_list


def test_add_dicts():
    answer = add_dicts({"dict_1_only": 1, "both_dicts": 2}, {"dict_2_only": 6, "both_dicts": 3})
    assert(answer == {"dict_1_only": 1, "both_dicts": 5, "dict_2_only": 6}), "add_dict broken"


def test_sum_list():
    answer = sum_list([[1], ["a", "b"], [{1: 2, 3: 4}], [[1, 2]]])
    assert (answer == [1, "a", "b", {1: 2, 3: 4}, [1, 2]]), "sum_list issue"


def test_figure_play_fact():
    line_1 = "2nd-10-OLI33PassManlio Conte pass under pressure from Leon Schnell. Incomplete."
    line_2 = "2nd-10-OLI19RushVlado Sindic runs for -1 yards. Tackled by Arian Dlouhý."
    line_3 = "2nd-10-ROS74SackDarrel Cope sacked by Leon Schnell for a loss of 3 yards"
    assert(figure_play_fact(line_1) == "-10-OLI33")
    assert(figure_play_fact(line_2) == "-11-OLI18")
    assert(figure_play_fact(line_3) == "-13-ROS71")


def test_calc_next_score():
    columns = ["7   TRA", "0   TRA", "3   TRA", "0   TRA", "0   TRA", "7   BEL", "3   BEL"]
    assert(calc_next_score(columns, 3) == -7)
