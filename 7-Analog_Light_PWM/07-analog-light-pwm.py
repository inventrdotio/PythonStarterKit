import machine
import utime

# Initialize button on GPIO 15
button = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)

# Initialize LED on GPIO 14 as a PWM pin
led = machine.PWM(machine.Pin(0))

# Predefined brightness levels (0-65535)
brightness_levels = [0, 8192, 16384, 32768, 65535]
current_level = 0

# Function to set the next brightness level
def set_next_brightness():
    global current_level
    current_level = (current_level + 1) % len(brightness_levels)
    led.duty_u16(brightness_levels[current_level])

# Main Loop
while True:
    if button.value() == 0:  # Button pressed
        set_next_brightness()
        utime.sleep_ms(200)  # Debounce button
    utime.sleep_ms(10)
