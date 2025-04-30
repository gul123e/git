
#---------------------------------------
#  Game Mechanics
#gul e sameen
#    Student A (team lead)
#---------------------------------------

def welcome_message():
    """
    Display the game's welcome message to the player.

    Parameters: None
    Returns: None
    """
   print("welcome to the game")
   print("you are the player")
   print("try to give correct answers")
   print("you win")
    
def choose_category(categories):
    """
    Ask the player to choose a quiz category from a list of categories.

    Parameters:
    - categories (list of str): A list of category names.

    Returns:
    - str: The chosen category.
    """
  print("choose catergory")
for i,c in enumerate(categories,1):
    print(f"{i}.{c}")
while True:
    choice=input():
    if choice.isdigit() and 1 <= int(choice) <=len(categories):
        return categories[int(choice)-1]
    else:
        print("invalid try again")
def display_score(score, round_number):
    """
    Display the current score and round number to the player.

    Parameters:
    - score (int): The player's current score.
    - round_number (int): The current round number.

    Returns: None
    """
    print(f"\ln Round(round_number)")
    print(f"current score :{score}\ln")
def game_over_message(final_score):
    """
    Display a "game over" message along with the player's final score.

    Parameters:
    - final_score (int): The player's final score at the end of the game.

    Returns: None
    """
    print(f"\ln game over")
    print(f"your final score is {final_score}")
    
    
def run_game_rounds(categories):
    """
    Implement a basic loop to run the game for 5 rounds.

    Parameters:
    - categories (list of str): A list of quiz categories.

    Returns: None
    """
    score=0
    round_number=1
    incorrect_answers=0
    welcome_message()
    while round_number<=5 and not check_game_over(incorrect_answers):
        display_score(score,round_number)
        category=choose_category(categories)
        print(f"you choose {category}")
   q=f"what is 2+3?"
   correct_answers="4"
   player_answer=input( f"{f}")
   if validate_answers(player_answer,correct_answer):
       print("correct\ln")
       score=update_score(score,True):
   else:
       print(f"{correct_answer}")
       score=update_score(score,False)
       incorrect_answers+=1
    if check_game_over(incorrect_answers):
        break
    round_number=next_round(round_number)
game_over_message(score)
restart_or_exit_()
       
     answer (correct or incorrect).

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the player's answer is correct, False otherwise.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def update_score(score, correct):
    """
    Implement a scoring system, where each correct answer awards points.

    Parameters:
    - score (int): The current score of the player.
    - correct (bool): Whether the player's answer was correct.

    Returns:
    - int: The updated score.
    """
  return score+10 if correct else score
def next_round(round_number):
    """
    Increase the round number after each question.

    Parameters:
    - round_number (int): The current round number.

    Returns:
    - int: The next round number.
    """
    return round_number+1

def check_game_over(incorrect_answers):
    """
    Implement a "game over" condition if the player makes 3 incorrect answers.

    Parameters:
    - incorrect_answers (int): The number of incorrect answers given by the player.

    Returns:
    - bool: True if the game should be over, False otherwise.
    """
    return  incorrect_answers>=3
def restart_or_exit():
    """
    Restart the game or exit after the game is over.

    Parameters: None
    Returns: None
    """
   choice=input()
   if choice=="yes":
       run_game_round(["math',"science","history"])
   else:
       print("thankyou for palying")
