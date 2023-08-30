import machine
import utime

# Initialize GPIO pin for LED
led = machine.Pin(14, machine.Pin.OUT)

# Initialize ADC for photoresistor
adc = machine.ADC(26)

# Threshold for ambient light level to turn on LED
LIGHT_THRESHOLD = 2000

# Function to read ambient light level
def read_light_level():
    return adc.read_u16()

# Main Loop
while True:
    light_level = read_light_level()
    
    # Turn on LED if light level is below threshold
    if light_level < LIGHT_THRESHOLD:
        led.value(1)
    else:
        led.value(0)
        
    utime.sleep_ms(500)  # Wait for 500 milliseconds before next reading
