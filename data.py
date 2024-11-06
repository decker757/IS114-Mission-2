import time
import requests
import serial
# Establish serial communication with micro:bit; replace with your serial port
# Note: 115200 is the baud rate for micro:bit
ser = serial.Serial('COM3', 115200)  
# API URL for updating ThingSpeak channel
url3 = "https://api.thingspeak.com/update.json"
api_key = 'VPS1BCH04YUJMUBJ' # Replace with your API key for the new lab8_2 channel
# Continuously read data from micro:bit
while True:
    # Read temperature value from micro:bit
  mbit_data = ser.readline()
  value = mbit_data.decode().strip()  # Convert bytes to string and strip leading/trailing whitespace
  # check if : is in the string
  if ":" in value:
    cycle = value.split(":")[1] # Split the string by ':', extract the second element (the temperature value).
  else:
    print('Serial data not in correct format')
    # Read light value from micro:bit
  datastring = {'api_key':api_key, 'field1':cycle}
  response = requests.post(url3, data=datastring)
  print(f"Sent data {datastring} to {url3}, got status code {response.status_code}")
  # *lab8_3* Append temperature, light data, and timestamp to index.html
  with open("data.html", "a") as indexfile:
    indexfile.write('<tr><td>'+cycle+'</td><td>'+time.ctime(time.time())+'</td></tr>\n')