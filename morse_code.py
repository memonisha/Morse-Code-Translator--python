morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

morse_to_char = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
    '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
    '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
    '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
    '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0',
    '/': ' '
}


def morseCode(text):
    result = ''
    upper = text.upper()
    for i in range(len(text)):
        for letter, morse in morse_code.items():
            if upper[i] == letter:
                result += morse + " "
    return result

def plainText(morse_code):
    result = ''
    morse_words = morse_code.split()
    
    for morse_word in morse_words:
        for morse, letter in morse_to_char.items():
            if morse_word == morse:
                result += letter
    return result.lower()
    

print("Morse Code Translator\n")
print('1. Morse Code\n2. Plain Text\n')
option = input("Do you want to translate to morse code or plain text? ")

if option == '1':
    text = input('Enter text to translate: ')
    print(f'Your translated text: {morseCode(text)}')
elif option == '2':
    morse_code_text = input('Enter text to translate: ')
    plainText(morse_code_text)
    print(f'Your translated text: {plainText(morse_code_text)}')
else:
    print('Invalid option. Please enter 1 for morse code or 2 for plain text!')