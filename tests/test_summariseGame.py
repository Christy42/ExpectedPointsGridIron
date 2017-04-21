import os

from expectedPoints.summariseGame import handle_fourth_down, get_final_scores


def test_handle_fourth_down():
    sample_string = [["1st-10-ROS31PassDarrel Cope pass under pressure from Joseba Aguirre. Incomplete.",
                      "2nd-10-ROS31PassDarrel Cope pass incomplete to Sean Fawl.",
                      "3rd-10-ROS31PassDarrel Cope pass to Francis Nugent for 7 yards."
                      "PuntDorival Canova punts the ball for 42 yards. "
                      "Joseph Dowds returns for 8 yards and is tackled by Jamsie McDaid."
                      "annic Steudler returns for 1 yards and is tackled by Saša Mirosavljev."],
                     ["1st-10-TRA34PassHunter Staten pass to Joseph Moss for 22 yards for a first down!",
                      "1st-10-TRA56PassHunter Staten pass incomplete to Torsten Dreier.",
                      "2nd-10-TRA56PassHunter Staten pass to Joseph Moss for 23 yards for a first down!",
                      "1st-10-TRA79PassHunter Staten pass incomplete to Joseph Moss.",
                      "2nd-10-TRA79PassHunter Staten pass incomplete to Rodolfo Belmonte.",
                      "3rd-10-TRA79PassHunter Staten pass incomplete to Joseph Moss."
                      "Field goalJoseph Moss 38 yard field goal is GOOD."
                      "KickoffJoseph Moss performs the kickoff. He kicks the ball for 65 yards. "
                      "Sean Fawl returns for 26 yards and is tackled by Gavin Hartery. "
                      "The offense will start on 69 yards from the end zone."]]
    answer = handle_fourth_down(sample_string)
    assert(answer[0][3][4:6] == "03")
    assert(answer[1][6][10:12] == "79")
    assert("field goal is GOOD" in answer[1][6])


def test_get_final_scores():
    with open(os.path.dirname(os.path.realpath(__file__)) + "//TestGame.txt", "r") as file:
        sample_game = file.read()
    answer = get_final_scores(sample_game)
    assert answer == [{"Score": 0, "Team": ""}, {"Score": 7, "Team": "ROS"}]
