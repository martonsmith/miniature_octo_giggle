letter_patterns = {
    "C": [5, 2, 2, 2, 5],
    "E": [6, 2, 4, 2, 6],
    "F": [6, 2, 4, 2, 2]
}

letter = ""
while letter != "QUIT":
    letter = input("Enter a letter (C, E, or F) or 'quit' to exit: ").upper()
    if letter in letter_patterns:
        for count in letter_patterns[letter]:
            print("X" * count)
    else:
        print("Letter not available.")
