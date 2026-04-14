"""
This project will build the Rock-Paper-Scissors game.

To run this game, please call "python RPS_Project.py" in your terminal. 
"""

from random import randint

option = ["ROCK", "PAPER", "SCISSORS"]
message = {
  "tie": "Yawn it's a tie!",
  "won": "Yay you won!",
  "lost": "Aww you lost!"
}

def decide_winner(user_choice, computer_choice):
  print "You selected: %s" % user_choice
  print "The computer selected: %s" % computer_choice
  if user_choice == computer_choice:
    print message["tie"]
  elif user_choice == option[0] and computer_choice == option[2]:
    print message["won"]
  elif user_choice == option[1] and computer_choice == option[0]:
    print message["won"]
  elif user_choice == option[2] and computer_choice == option[1]:
    print message["won"]
  else:
    print message["lost"]

def play_RPS():
  user_choice = raw_input("Enter rock, paper, or scissors: ")
  user_choice = user_choice.upper()
  computer_choice = option[randint(0, 2)]
  decide_winner(user_choice, computer_choice)
  
play_RPS()