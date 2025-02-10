import re

while True:
    weight = input("Add your weight with unit of measure (e.g., 70 kg or 150 lbs): ")
    match = re.match(r"(\d+)\s*(kg|lbs)", weight)

    if match:
        value = int(match.group(1))
        unit = match.group(2)

        if unit == "lbs":
            converted_weight = value * 0.45
            print(f"You are {converted_weight} in kilos.")
            break
        elif unit == "kg":
            converted_weight = value / 0.45
            print (f"You are {converted_weight} in pounds.")
            break
    else:
        print("Invalid input format. PLease enter a number followed by space  and unit (kg or lbs).")