""" Python Study Game, This is a program desgioned to helpo students prepawre and study for 
    specfic topics or courses. They will battle against themselves (Time) in order to complete 
    the questions and get their highscore. 
    In order to run this program you will next a questions.txt file.
    This file will have the questions in the correct format (level,type,questions,answer)
    Example Fill In The Blank: 1,f,What is the capital of Colombia?, Bogota
    Example Multiple Choice: 2,m,Immigrants entering the U.S through California had to go through 
                             immigration stations on,3,ellis island, alcatraz island, angel island, rhode island
Driver: Felipe Martinez
Navigator: Adam Yassir 
Assignment: Final Project
Date: 5_13_22
Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import sys
from threading import Timer
import argparse

#Global Variables 
CONTINUE = True
TOTALQUESTIONS = 1
TOTALANSWERED = 0
TOTALCORRECT = 0

class StudyGame():
    """ Study Game, reads from a file to obtain the questions/answers for the program.
    Has methods in order to read questions. Ex: Multiple choice
    Args:
        Attributes: self:The StudyGame
    """
    def __init__(self):
        """ Initializes the StudyGame. Creates an empty list that will be used to store the game questions
        Args:
            self: StudyGame
        """
        self.gamelist = []

    def readQuestions(self,testfile):
        """ Takes and reads from a file. Seperates the file based on each (,) for each line,
            Each line represents a new question for the game. 
        Args:
            testfile: File being passed in; contains the questions/answser for the game
        """
        fp = open(testfile)
        for line in fp:
            line =line.strip()
            tlist = line.split(",")
            self.gamelist.append(tlist)


    def multipleChoice(self,list):
        """ If question is a multiple choice type, it will p;rint the level and question from the game list.
            Asks user to ebnter a number for the correct answer and saves it into studentanswer.
        Args:
            self: The StudyGame
            list: list containing the game questions/answers
        Returns:
                studentanswer: user choice for the multiple choice question (int)
        """
        questiontyp = list[1]
        level = list[0]
        question = list[2]
        answer = list[3].lower()
        print(f" Level {level}: {question}: ")
        mchoice = list[4:]
        for i   in range(len(mchoice)):
            print(f"{i + 1}. {mchoice[i]}",end=" ")
        print()
        studentanswer = input("Enter your choice: ")
        return studentanswer
    
def stopTest():
    """ Method used to stop the game. Once game is stopped, it will print out Times up!
        It will also print the users total answered questions out of the total questions.
        It will present the user with their score as a percent. 
        """
    CONTINUE = False
    print()
    print("Times up!!")
    print(f"You answered {TOTALANSWERED} questions out of {TOTALQUESTIONS}  and got {TOTALCORRECT} correct")
    print(f"your score is {TOTALCORRECT / TOTALQUESTIONS * 100:.0f}%")

def startTimer(timelimit):
    """ Creates The StudyGame Timer with the timelimit choosen by the user.
        Args:
            timelimit: The time limit for the game. Chosen by the user when running program. 
        Returns:
                timer: The Timer for the game.
    """      
    timer = Timer(interval=timelimit,function=stopTest)
    return timer

def main(name, timelimit, path):
    """ Main, it creates a new game for the user to play. It starts the timer for the game. It prints out
        a message with instructions on how the game is played and provides information for the user.
        It uses the games list in order to check the fill in the blank questions. 
        Args:
            name: The Users Name
            timelimit: The time limit for the game. Chosen by the user when running program.
            path: The file that contains all the questions/answer for the game =
        """
    global TOTALQUESTIONS
    global TOTALCORRECT
    global TOTALANSWERED
    game = StudyGame()
    qlist = game.readQuestions(path)
    TOTALQUESTIONS = len(game.gamelist)
    timer = startTimer(timelimit)
    questionnumber = 0
    timer.start()
    print(
        name + " Welcome to the Study Game! \nThis is a game designed to help you study for your class and have fun doing it!\nThere are three levels to this game, each level has unique questions to ask you and gets harder as you advance.\nEach question is worth points, but you can score more if you answer them faster.\nYou will be timed in order to challenge you and help your progress by comparing highscores.")
    print(f"You have {timelimit/60} minutes to finish the test. Good luck!!\n")
  
    while CONTINUE:
        questiontype = game.gamelist[questionnumber][1]
        level = game.gamelist[questionnumber][0]
        question = game.gamelist[questionnumber][2]
        answer = game.gamelist[questionnumber][3].lower()
        if questiontype == "f":
           studentanswer = input(f" Level {level}: {question}: ").lower().strip()
        else:
            studentanswer = game.multipleChoice(qlist)
        TOTALANSWERED += 1
        if answer == studentanswer:
            TOTALCORRECT += 1
        questionnumber += 1
        if questionnumber == TOTALQUESTIONS:
            timer.cancel()
            print(f"You answered {TOTALANSWERED} questions out of {TOTALQUESTIONS}  and got {TOTALCORRECT} correct")
            print(f"your score is {TOTALCORRECT / TOTALQUESTIONS * 100:.0f}%")
            break

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as
        arguments
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """ 
    parser = argparse.ArgumentParser()  
    parser.add_argument('player_name', type=str, help="Please enter Player Name")
    parser.add_argument('time_limit', type=int, help="Please enter Time limit (180Seconds(HARD)(3Min),360Seconds(MEDIUM)(6Min),600Seconds(EASY)(10Min))")
    parser.add_argument('path', type=str, help="Please enter the path in order to obtain questions for the game")
    args = parser.parse_args(args_list)  # We need to parse the list of command line
    return args

if __name__ == "__main__":
     arguments = parse_args(sys.argv[1:])  
     main(arguments.player_name, arguments.time_limit, arguments.path)
 
