import random

def guess_number():
    min_attempts = float('inf')

    while True:
        user_attempts = 0
        pc_choice = random.randint(1, 10)

        while True:
            user_choice = int(input('Pick a number from 1-10: '))
            user_attempts += 1

            if user_choice < pc_choice:
                print('Higher')
            elif user_choice > pc_choice:
                print('Lower')
            else:
                break

        print(f"Congratulations! You guessed the number in {user_attempts} attempts.")
        
        if user_attempts < min_attempts:
            min_attempts = user_attempts
            
        print(f"The minimum number of attempts so far is {min_attempts}")
        
        play_again = input("Do you want to play again? (yes/no) ").lower()
        if play_again == "no":
            break

if __name__ == "__main__":
    guess_number()
