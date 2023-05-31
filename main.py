# Text to International Morse Code Translator

# morse_code_dict contains the translations for each character of the user's input string

morse_code_dict = {
    " ": "/",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
    "$": "...-..-",
    "@": ".--.-.",
    "¿": "..-.-",
    "¡": "--...-"
}

# Program introduces rules to the user

print("International Morse Code Translator: Works with all letters, numbers, and most punctuation symbols")
print("Spaces between words are denoted with '/' to separate words in the translation. Spaces are present between"
      " characters of the translation")

# User inputs their requested text, which is set to lowercase in order to work with morse_code_dict

user_input = input("Please enter the text that you would like translated into morse code: ").lower()

# for loop finds the value from each character key, then adds it to the new translation string

translation = ""
for char in user_input:
    try:
        translation += morse_code_dict[char]

        # Adding a space between characters of a word in the translation

        translation += " "
    except KeyError:

        # Error message for whenever the user inputs an unsupported character

        print(f"Sorry, the symbol '{char}' is not supported")

print(f"Translation: {translation}")
