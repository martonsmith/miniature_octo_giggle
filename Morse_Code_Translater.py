#Morse Code Dictionary
morse_code_dic = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',

    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}

#Function to convert Text to Morse
def text_to_morse(text):
    morse_code = ""
    for char in text.upper():
        if char in morse_code_dic:
            morse_code += morse_code_dic[char] + " "
        else:
            morse_code += "/ "
    return morse_code.strip()

#Function to convert Morse to Text
def morse_to_text(morse):
    text = ""
    words = morse.strip().split(" / ")

#Reversing the dictionary
    morse_code_dictionary_reverse = {morse: symbol for symbol, morse in morse_code_dic.items()}

    for word in words:
        for char in word.split(" "):
            if char in morse_code_dictionary_reverse:
                text += morse_code_dictionary_reverse[char]
            else:
                text += "?"
        text += " "
    return text.strip()

#Main function which interact with the user
def morse_code_translator():
    print("Welcome to the Morse Translator")
    print("You can write your text here and translate it to Morse code or vice versa")

    while True:
        user_text = input("If you want to translate Morse code to Text write 'morse' or if you want to translate Text to Morse Code write 'text': ").strip().lower()

        if user_text == "morse":
            morse = input("Write here your morse code: ").strip()
            print(f"Text: {morse_to_text(morse)}")

        elif user_text == "text":
            text = input("Write here your text: ").strip()
            print(f"Morse Code: {text_to_morse(text)}")
        else:
            print("Invalid command. Please enter 'text' or 'morse'")

        again = input("Would you like to convert again? (Y/N)").strip().lower()
        if again != 'y':
            print("See you later")
            break
morse_code_translator()