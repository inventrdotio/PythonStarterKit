import machine
import utime

# Initialize LEDs
cold_led = machine.Pin(10, machine.Pin.OUT)
moderate_led = machine.Pin(11, machine.Pin.OUT)
hot_led = machine.Pin(12, machine.Pin.OUT)

# Initialize ADC for the internal temperature sensor
adc = machine.ADC(4)
conversion_factor = 3.3 / (65535)

# Function to read temperature
def read_temperature():
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    return temperature

# Main Loop
while True:
    temperature = read_temperature()
    print("Current temperature: ", temperature, "°C")

    # Reset all LEDs
    cold_led.value(0)
    moderate_led.value(0)
    hot_led.value(0)

    # Temperature indicator logic
    if temperature < 20:
        cold_led.value(1)
    elif 20 <= temperature < 30:
        moderate_led.value(1)
    else:
        hot_led.value(1)
        
    utime.sleep(2)
