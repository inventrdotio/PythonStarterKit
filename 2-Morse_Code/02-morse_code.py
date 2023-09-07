import machine
import time

# Define the GPIO pin for the button
button_pin = 15
button = machine.Pin(button_pin, machine.Pin.IN, machine.Pin.PULL_UP)

# Morse code mapping
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

dot_duration = 0.2
dash_duration = 0.6
end_of_letter_duration = 1.5

def interpret_button_press():
    morse_string = ''
    while True:
        while button.value() == 1:
            time.sleep(0.05)

        # Measure the duration of the button press
        start_time = time.time()
        while button.value() == 0:
            pass
        end_time = time.time()
        duration = end_time - start_time

        if duration <= dot_duration:
            morse_string += '.'
        else:
            morse_string += '-'
        
        # Wait to see if the user finishes inputting the letter
        start_time = time.time()
        while button.value() == 1:
            if (time.time() - start_time) > end_of_letter_duration:
                return morse_string

def main():
    print("Input Morse code using the button. A short press is '.', a long press is '-'.")
    print("Wait for more than 1.5 seconds to finish inputting a letter.")
    
    while True:
        morse_string = interpret_button_press()
        for key, value in morse_code.items():
            if value == morse_string:
                print(key)
                break
        else:
            print(f"Unrecognized Morse code: {morse_string}")

if __name__ == "__main__":
    main()

