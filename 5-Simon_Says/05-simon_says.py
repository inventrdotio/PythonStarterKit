import machine
import utime
import urandom

# Initialize LEDs
led_pins = [10, 11, 12, 13]
leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

# Initialize buttons
button_pins = [14, 15, 16, 17]
buttons = [machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP) for pin in button_pins]

# Generate a random sequence
sequence = [urandom.randint(0, 3) for _ in range(5)]

# Function to show the sequence using LEDs
def show_sequence():
    for num in sequence:
        leds[num].value(1)
        utime.sleep_ms(500)
        leds[num].value(0)
        utime.sleep_ms(500)

# Function to get player's input and check if it's correct
def get_input():
    player_sequence = []
    while len(player_sequence) < len(sequence):
        for i, button in enumerate(buttons):
            if button.value() == 0:
                player_sequence.append(i)
                leds[i].value(1)
                utime.sleep_ms(300)
                leds[i].value(0)
                utime.sleep_ms(200)
                if player_sequence[-1] != sequence[len(player_sequence) - 1]:
                    return False
    return True

# Main game loop
while True:
    show_sequence()
    if get_input():
        print("You win!")
    else:
        print("You lose!")
    utime.sleep(2)
