from art import logo
from codes import letter_morse_codes


# TODO 2 Convert letter to morse code
def text_to_code(text, codes):
    letters = [key for key in codes.keys()]

    for char in text:
        if char in letters:
            text = text.replace(char, codes[char])

    return text


# TODO 1 Request for user input
# print(logo)
text_to_convert = input("Enter the text you would like to convert to Morse Code: ")
morse_code = text_to_code(text_to_convert, letter_morse_codes)
print(morse_code)

