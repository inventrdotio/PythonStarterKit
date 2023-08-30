import machine
import utime

# Initialize GPIO pins for LEDs
red_led = machine.Pin(16, machine.Pin.OUT)
yellow_led = machine.Pin(17, machine.Pin.OUT)
green_led = machine.Pin(18, machine.Pin.OUT)

# Function to turn all LEDs off
def all_off():
    red_led.value(0)
    yellow_led.value(0)
    green_led.value(0)

# Main Loop
while True:
    all_off()  # Turn all LEDs off
    
    red_led.value(1)  # Turn red LED on
    utime.sleep(5)  # Wait for 5 seconds
    
    all_off()  # Turn all LEDs off
    
    yellow_led.value(1)  # Turn yellow LED on
    utime.sleep(1)  # Wait for 1 second
    
    all_off()  # Turn all LEDs off
    
    green_led.value(1)  # Turn green LED on
    utime.sleep(4)  # Wait for 4 seconds