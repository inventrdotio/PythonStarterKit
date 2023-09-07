import machine
import time

# Define LED Pin
LED_PIN = 17
led = machine.Pin(LED_PIN, machine.Pin.OUT)

# Define ADC Pin for LDR
ADC_PIN = 26
adc = machine.ADC(machine.Pin(ADC_PIN))

# Define a threshold for the LDR reading below which the LED should turn ON
LIGHT_THRESHOLD = 50000  # This might need adjustment based on your LDR and environment

def night_light():
    while True:
        light_value = adc.read_u16()
        print(light_value)
        # If the reading is below the threshold, turn the LED on. Otherwise, turn it off.
        if light_value < LIGHT_THRESHOLD:
            led.value(1)
        else:
            led.value(0)
        
        time.sleep(0.5)  # Check every half second

night_light()

