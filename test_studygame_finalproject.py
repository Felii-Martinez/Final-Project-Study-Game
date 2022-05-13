""" Python Study Game Unit Test, Provides some unit test in order to test
    study_game_finalproject methods.
Driver: Felipe Martinez
Navigator: Adam Yassir 
Assignment: Final Project
Date: 5_13_22
Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from study_game_finalproject import *
def test_readQuestions():
    """ Tests for gathering the questions from a file. If the questions equal 21 (Number of question for this game)
        Then it passes
    """
    print("test creating Tester object reading questions")
    game = StudyGame()
    testfile = "questions.txt"
    game.readQuestions(testfile)
    print(game.gamelist)
    assert len(game.gamelist) == 21


def test_timer():
    """ Tests the timer for the game
    """
    print("test timer")
    global CONTINUE
    global  TOTQUESTS
    t =startTimer(6)
    i = 0
    TOTQUESTS = 2
    t.start()
    while CONTINUE:
        i += 1
    assert CONTINUE == True

def test_multiple_choice():
    """ Tests for the multiple choice answer. Passes, after providing the correcrt choice (2) for the last question
    """
    print("test multiple choice")
    game = StudyGame()
    testfile = "questions.txt"
    game.readQuestions(testfile)
    answer = game.multipleChoice(game.gamelist[20])
    assert answer == "2"


test_readQuestions()
test_multiple_choice()
test_timer()
