def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
    return(celsius * 9 / 5) +32

#Initialize variable and ask for temperature with unit
temperature = ""

while temperature != "quit":
    temperature = input("Enter temperature (e.g.: 30C or 70F) or type 'quit' to exit: ")

    #If the user type 'quit' break the loop
    if temperature == "quit":
        break
    #Chek if the input is valid (contains a number and a unit)
    if len(temperature) < 2 or not temperature[-1].isalpha():
        print("Invalid input! Please enter valid temperature with 'C' or 'F' at the end.")
        continue

    #Extract the number and the unit
    number = float(temperature[:-1])
    unit = temperature[-1]

    #Convert based on the unit
    if unit == "f":
        converted = fahrenheit_to_celsius(number)
        print(f"{number} Fahrenheit is equal to {converted} Celsius")
    elif unit == "c":
        converted = celsius_to_fahrenheit(number)
        print(f"{number} Celsius is equal to {converted} Fahrenheit")
    else:
        print("Invalid unit! Please use 'F' or 'C' after the number.")



