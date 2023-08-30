import machine
import utime

# Initialize button
button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

# Initialize LEDs
led_pins = [14, 16, 17, 18]
leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

# Initialize counter
counter = 0

# Function to display counter in binary on LEDs
def display_counter(counter):
    for i in range(4):
        leds[i].value((counter >> i) & 1)

# Main Loop
while True:
    if button.value() == 0:  # Button pressed
        counter = (counter + 1) % 16  # Increment counter, reset to 0 if it reaches 16
        display_counter(counter)  # Update LED display
        utime.sleep_ms(200)  # Debounce button
        
    utime.sleep_ms(10)
