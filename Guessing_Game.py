import random

#Function to play the game
def play_game():
    secret_number = random.randint(1, 10)
    guess_count = 0
    guess_limit = 4

#Loop for guesses
    while guess_count < guess_limit:
        guess = int(input("Guess between 1-10: "))
        guess_count += 1

        if guess == secret_number:
            print("Congratulation! You guessed it!")
            return True    #Info for next loop
        elif guess < secret_number:
            print("Too low.")

        elif guess > secret_number:
            print("Too high.")
    print(f"Out of attempts! The correct number was {secret_number}")
    return False   #Info for next loop

#Loop for play again, Check if the user want to play again
while True:
    if play_game():  #If the game was won
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break   #Exit the loop if no play again
    else:   #If the game was lost
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again != "yes":
            print("Thanks for playing")
            break   #Exit the game if no play again
