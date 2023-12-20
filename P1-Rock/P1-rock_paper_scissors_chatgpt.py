import random

# list of play options
options = ["rock", "paper", "scissors"]

# winning rules
rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

while True:
    # get player choice
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    
    # check if player choice is valid
    if player_choice not in options:
        print("Invalid choice. Please try again.")
        continue
    
    # get computer choice
    computer_choice = random.choice(options)
    
    # print player choice and computer choice
    print(f"Player's choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}")
    
    # check the result 
    if player_choice == computer_choice:
        print("It's a tie!")
    elif rules.get(player_choice) == computer_choice:
        print("You win!")
# rules.get(player_choice): This part retrieves the value associated with the key player_choice from the rules dictionary.
# In the context of rock-paper-scissors, player_choice is the choice made by the player (e.g., "rock", "paper", or "scissors"). 
# This dictionary contains the winning conditions where keys represent player choices and values represent the choices that they defeat. 
# For example, if the player chooses "rock", rules.get("rock") would return "scissors" because "rock" beats "scissors".
# == computer_choice: This part compares the value retrieved from the dictionary (rules.get(player_choice)) with the computer_choice, 
# which is the randomly selected choice made by the computer.

# if rules.get(player_choice) == computer_choice:

# If the player's choice defeats the computer's choice based on the rules defined in the rules dictionary, this condition is True.
# In this case, the message "You win!" is printed, indicating that the player wins the round.
    else:
        print("You lose!")
