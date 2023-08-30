import machine
import utime
import urandom

# Initialize GPIO pins for LED and Button
led = machine.Pin(14, machine.Pin.OUT)
button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

# Function to get a random delay time
def get_random_delay():
    return urandom.randint(3, 7)

# Main Loop
while True:
    led.value(0)  # Turn LED off initially
    
    # Wait for a random amount of time
    utime.sleep(get_random_delay())
    
    # Turn on the LED
    led.value(1)
    
    # Record the time the LED turned on
    start_time = utime.ticks_ms()
    
    # Wait for button press
    while button.value() == 1:
        pass
    
    # Record the time the button was pressed
    end_time = utime.ticks_ms()
    
    # Turn off the LED
    led.value(0)
    
    # Calculate reaction time
    reaction_time = utime.ticks_diff(end_time, start_time)
    
    print("Your reaction time is:", reaction_time, "ms")
    
    # Wait before the next iteration
    utime.sleep(2)
