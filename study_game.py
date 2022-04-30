""" Python Study Game
Driver: Felipe Martinez
Navigator: Adam Yassir 
Assignment: Final Project
Date: 4_25_22
Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from operator import le
import random
import time
import sys
import argparse
import datetime


class Game:
    """ Game class, it includes the study questions and the timer for the game
    Args:
        Attributes : timer; instantiate the game with timer. 
    """

    def __init__(self, time_limit):
        """
         Initializes a Game

        Args:
            time_limit: Choose the time limit when creating game; takes in second (Must convert to minutes)
 
        """
        self.time_limit = time_limit
        minutes = self.time_limit * 60    #convert sec into min
        while minutes > 0:
            timer = datetime.timedelta(seconds = minutes)
            print(timer, end="\r")
            time.sleep(1)
            minutes -= 1
        print("Game Over")
    
        
 
   
        

    # def game_timer(time_limit):
        """
        Timer class, converts seconds into minutes

        Args:
            time_limit: Choose the time limit when creating game; takes in second (Must convert to minutes)

        """
        minutes = time_limit * 60    #convert sec into min
        start_time = time.time()
        elapsed_time = time.time() - start_time
        print(minutes - int(elapsed_time))
        if elapsed_time > minutes:
            print("Game Over")

    def __repr__(self):
        return "Study Game".format(self=self)
    
    

    def study_questions_level_two():
        """
        Study questions; level two (Medium)
        
        Returns:
            One question at a time (No Duplicate Questions)

        """
        questions_asked = []
        value = random.randint(11,20)
        questions = {11:"What is the capital of California?", 12:"What is the capital of Germany?", 13: 
          "What is the capital of Colombia?", 14: "What is the capital of Australia?", 15:
          "What is the capital of Poland?", 16: "What is the capital of Denmark?", 17:
          "What is the capital of Brazil?", 18: "What is the capital of South Africa?", 19: "What is the capital of New Zealand?", 20:
          "What is the capital of Mexico?"}
        
        for question in questions:
            if value is not questions_asked:
                return questions.get(value)
            else:
                questions_asked.append(value) #No repeated questions

    def study_questions_level_three():
        """
        Study questions; level three (Hard)
        
        Returns:
            One question at a time (No Duplicate Questions)

        """
        questions_asked = []
        value = random.randint(21,30)
        questions = {21:"What is the capital of California?", 22:"What is the capital of Germany?", 23: 
          "What is the capital of Colombia?", 24: "What is the capital of Australia?", 25:
          "What is the capital of Poland?", 26: "What is the capital of Denmark?", 27:
          "What is the capital of Brazil?", 28: "What is the capital of South Africa?", 29: "What is the capital of New Zealand?", 30:
          "What is the capital of Mexico?"}
        
        for question in questions:
            if value is not questions_asked:
                return questions.get(value)
            else:
                questions_asked.append(value) #No repeated questions

def study_questions_level_one():
        """
        Holds all the Study questions for level one (Easy)
        
        Returns:
            A dictionary with the study questions

        """
        questions = {1:"What is the capital of Spain?", 2:"What is the capital of Germany?", 3: 
          "What is the capital of Colombia?", 4: "What is the capital of Australia?", 5:
          "What is the capital of Poland?", 6: "What is the capital of Denmark?", 7:
          "What is the capital of Brazil?", 8: "What is the capital of South Africa?", 9: "What is the capital of New Zealand?", 10:
          "What is the capital of Mexico?"}
        
        return questions 

def main(player_name, time_limit):
    """
        Main; creates a new game with instructions. Gathers the questions for the user and lets the user respond to the questions. 
        Provides the user with their score at the end of the game.
        """
    print(player_name + " Welcome to the Study Game! \nThis is a game designed to help you study for your class and have fun doing it!\nThere are three levels to this game, each level has unique questions to ask you and gets harder as you advance.\nEach question is worth points, but you can score more if you answer them faster.\nYou will be timed in order to challenge you and help your progress by comparing highscores.")

    #new_game = Game(time_limit)  #Creates Game with timer already built in
    #print(new_game)
    player_score = 0  #Player's score counter  
    level_one_questions = study_questions_level_one() 
    print("\n--------Level One--------")
    print("Lets test your geography!\n")

    question_one_answer = input(level_one_questions[1]+" " + player_name +", your answer is: ")
    if question_one_answer.lower() == "madrid":
        player_score += 3
    question_two_answer = input(level_one_questions[2]+" " + player_name +", your answer is: ")
    if question_two_answer.lower() == "berlin":
        player_score += 3
    question_three_answer = input(level_one_questions[3]+" " + player_name +", your answer is: ")
    if question_three_answer.lower() == "bogota":
        player_score += 3
    question_four_answer = input(level_one_questions[4]+" " + player_name +", your answer is: ")
    if question_four_answer.lower() == "canberra":
        player_score += 3
    question_five_answer = input(level_one_questions[5]+" " + player_name +", your answer is: ")
    if question_five_answer.lower() == "warsaw":
        player_score += 3
    question_six_answer = input(level_one_questions[6]+" " + player_name +", your answer is: ")
    if question_six_answer.lower() == "copenhagen":
        player_score += 3
    question_seven_answer = input(level_one_questions[7]+" " + player_name +", your answer is: ")
    if question_seven_answer.lower() == "brasilia":
        player_score += 3
    question_eight_answer = input(level_one_questions[8]+" " + player_name +", your answer is: ")
    if question_eight_answer.lower() == "pretoria":
        player_score += 3
    question_nine_answer = input(level_one_questions[9]+" " + player_name +", your answer is: ")
    if question_nine_answer.lower() == "wellington":
        player_score += 3
    question_ten_answer = input(level_one_questions[10]+" " + player_name +", your answer is: ")
    if question_ten_answer.lower() == "mexico city":
        player_score += 3

    if player_score > 25:
        print("\nAmazing job! I can see you definitely studied!\nScore:")
        print(player_score)
    
    if player_score < 25 and player_score > 15:
        print("\nGreat try! Study and comeback and you will surley do better!\nScore:")
        print(player_score)

    if player_score < 15:
        print("\nYou definitely need to study more! study some of the questions and come back to do better!\nScore:")
        print(player_score)


    #i  = 1
    #for i in level_one_questions:        
        #player_answer_one = input(level_one_questions[i]+" " + player_name +", your answer is: ")
        #i  += 1     
    
def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as
        arguments
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    #For the sake of readability it is important to insert comments all throughout.
    #Complicated operations get a few lines of comments before the operations
    #Non-obvious ones get comments at the end of the line.
    #For example:
    #This function uses the argparse module in order to parse command line arguments.
    parser = argparse.ArgumentParser() #Create an ArgumentParser object.
    #Then we will add arguments to this parser object.
    #In this case, we have a required positional argument.
    #Followed by an optional keyword argument which contains a default value.
    parser.add_argument('player_name', type=str, help="Please enter Player Name")
    parser.add_argument('time_limit', type=int, help="Please enter Time limit (5(HARD),10(MEDIUM),15(EASY))")
    args = parser.parse_args(args_list) #We need to parse the list of command line
    return args

if __name__ == "__main__":   
    arguments = parse_args(sys.argv[1:]) #Pass in the list of command line arguments to the parse_args function
    #The returned object is an object with those command line arguments as attributes of an object.
    #We will pass both of these arguments into the main function.
    #Note that you do not need a main function, but you might find it helpfull.
    #You do want to make sure to have minimal code under the 'if __name__ == "__main__":' statement.
    main(arguments.player_name, arguments.time_limit)

