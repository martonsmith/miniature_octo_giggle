#Function to check if the user allowed to drive based on age
def check_age(age):
    if age < 18:
        print("You are underage.")
        return False
    elif age >= 65:
        conditions = input("Do you have any conditions that would prevent you from driving safely? (yes/no): ").strip().lower()
        if conditions == "yes":
            return False
        else:
            print("You are a senior citizen may eligible for senior discounts and programs!")
            return True
    else:
        print("You are an adult.")
        return True

#Function to check if the user has a driver's license
def check_license():
    license_input = input("Do you have driver's license? (yes/no): ").strip().lower()
    return license_input == "yes"

#Main function to organize the logic flow of the program
def main():
    age = int(input("How old are you: "))

    if check_age(age):  # If the use eligible based on age
        if check_license():  #If the user has license
            print("You are allowed to drive.")
        else:
            print("You need to get driver's license before you can drive")
    else:
        print("Sorry, you're not eligible to drive yet.")
main()