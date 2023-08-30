import machine
import utime

# Initialize GPIO pins for LED and Button
led = machine.Pin(14, machine.Pin.OUT)
button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

# Constants for Morse Code
DOT_LENGTH = 200  # 200ms for dot
DASH_LENGTH = 600  # 600ms for dash
PAUSE_LENGTH = 200  # 200ms pause between dots and dashes
LONG_PAUSE_LENGTH = 600  # 600ms pause between letters

# Function to blink the LED
def blink(duration):
    led.value(1)
    utime.sleep_ms(duration)
    led.value(0)
    utime.sleep_ms(PAUSE_LENGTH)

# Main Loop
while True:
    if button.value() == 0:  # Button pressed (pull-down)
        press_time = utime.ticks_ms()  # Record the time when button is pressed
        
        # Wait for button to be released
        while button.value() == 0:
            pass
        
        # Calculate how long the button was held down
        hold_time = utime.ticks_diff(utime.ticks_ms(), press_time)
        
        # Short press for dot
        if hold_time < 400:
            blink(DOT_LENGTH)
        # Long press for dash
        else:
            blink(DASH_LENGTH)
        
        utime.sleep_ms(LONG_PAUSE_LENGTH)
