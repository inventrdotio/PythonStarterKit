import machine
import utime
import urandom

# Initialize LEDs
led_pins = [12, 13]
leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

# Initialize buttons
button_pins = [14, 15]
buttons = [machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP) for pin in button_pins]

# This function will flash the given LED number
def flash_led(led_number, duration=0.5):
    leds[led_number].value(1)
    utime.sleep(duration)
    leds[led_number].value(0)
    utime.sleep(duration)

# This function waits for a button press and returns the button number
def wait_for_button():
    while True:
        for i, button in enumerate(buttons):
            if button.value() == 0:
                # Debounce the button press
                utime.sleep_ms(20)
                while button.value() == 0:
                    pass
                return i

# Main game loop
sequence = []
while True:
    print("\nNew round! Watch the LED sequence...")
    
    # Add a new step to the sequence
    sequence.append(urandom.randint(0, 1))
    
    # Show the sequence to the player
    for led_number in sequence:
        flash_led(led_number)
    
    print("Now, replicate the sequence using the buttons!")
    
    # Wait for player's input and check if it's correct
    for led_number in sequence:
        button_number = wait_for_button()
        if button_number != led_number:
            # Wrong sequence, flash both LEDs as an error signal and restart the game
            flash_led(0, 0.2)
            flash_led(1, 0.2)
            print("Wrong sequence! Let's start over.")
            sequence = []
            break
        else:
            print(f"Correct button {button_number+1}!")
    
    # Inform player about the correct sequence input
    if len(sequence) > 0 and button_number == led_number:
        print(f"Good job! Sequence length is now {len(sequence)}")
    
    # Small delay before next sequence
    utime.sleep(1)

