import machine
import network
import utime
import urequests

# Your ThingSpeak API Key and channel
API_KEY = "YOUR_THINGSPEAK_API_KEY"
CHANNEL_ID = "YOUR_THINGSPEAK_CHANNEL_ID"

# Connect to WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Your_WiFi_Name", "Your_WiFi_Password")
while not wlan.isconnected():
    utime.sleep(1)

# Read temperature from internal sensor
adc = machine.ADC(4)  # Pin for the built-in temperature sensor is 4
conversion_factor = 3.3 / (65535)
def read_temperature():
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    return temperature

# Main loop
while True:
    temperature = read_temperature()
    print("Temperature:", temperature, "°C")

    # Report the data to ThingSpeak (replace with your ThingSpeak channel and API key)
    url = "http://api.thingspeak.com/update"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "api_key": API_KEY,
        "field1": temperature
    }
    response = urequests.post(url, headers=headers, data=data)
    print(response.text)
    
    # Wait for a bit before the next reading
    utime.sleep(10)
