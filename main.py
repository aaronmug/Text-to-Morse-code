from art import logo
from codes import letter_morse_codes


def text_to_code(text, codes):
    # Create an empty string to store the Morse code representation
    morse_code = []

    # Create a list of keys from the imported codes dictionary
    letters = [key for key in codes.keys()]

    # loop through each char in the input text and check if it's in the keys list
    for char in text:
        if char in letters:
            morse_code.append(codes[char])

    return " ".join(morse_code)


def convert_text(string):
    # TODO 2 Convert input to morse code using a function
    morse_code = text_to_code(string, letter_morse_codes)
    # TODO 4 Output the morse code of the input text
    print(morse_code)


print(logo)

is_converting = True

# TODO 5 Enable the user to continue converting text
while is_converting:
    # TODO 1 Request for user input
    text_to_convert = input("Enter the text you would like to convert to Morse Code: ").upper()
    convert_text(text_to_convert)
    continue_converting = input("Convert more text(y/n): ").lower()
    if continue_converting == 'y':
        convert_text(text_to_convert)
    elif continue_converting == 'n':
        is_converting = False
