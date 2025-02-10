#Function for logic of game
def car_game():
    command = ""
    started = False   #Tracking when the car is started
    print("""
Welcome to the Car Game
Write Your Commands after '> ':
start - to start the car
stop - to stop the car
status - to check the car's status
quit - to end the game
help - to show commands""")

    #Main loop for game
    while True:
        command = input("> ").lower()

        if command == "start":
            if started:
                print("Car is already started.")
            else:
                started = True
                print("Car started. Ready to roll.")

        elif command == "stop":
            if not started:
                print("Car is already stopped.")
            else:
                started = False
                print("Car stopped.")
        elif command == "status":
            if started:
                print("The car is currently started.")
            else:
                print("The car is currently stopped.")

        elif command == "help":
            print("""
start - to start the car
stop - to stop the car
status - to check the car's status
quit - to end game
help - to show commands""")

        elif command == "quit":
            break

        else:
            print("Sorry, I don't understand your command")

#Runs the function
car_game()




