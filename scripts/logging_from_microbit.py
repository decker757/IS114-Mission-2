import time
import requests
import serial
import base64
import serial.tools.list_ports

def get_com_port_universal():
    # return first port
    ports = serial.tools.list_ports.comports()
    print(ports)
    if len(ports) != 0:
        return ports[0].name
    else:
        return None

def get_variable_and_value(string):
    # returns variable value pair if the string from microbit is valid
    try:
        first, second = value.split(':')
        return first, second
    except:
        print('Serial data not in correct format')
        return None
        

WRITE_API_KEY_BASE_64 = "VlBTMUJDSDA0WVVKTVVCSg=="
WRITE_API_KEY = base64.b64decode(WRITE_API_KEY_BASE_64).decode()
COM_PORT = "COM5"
BAUD_RATE = 115200
POST_URL = "https://api.thingspeak.com/update.json"
API_FIELDS = {"cycle":"field1", 'slouch':"field2"}

# initialise serial connection
ser = serial.Serial(COM_PORT, BAUD_RATE)
# continuously read from com port, 1 while loop 1 cycle
while True:

    # Read cycle value from micro:bit
    line_of_mbit_data = ser.readline()
    
    # Convert bytes to string and strip leading/trailing whitespace
    cleaned_line_of_mbit_data = line_of_mbit_data.decode().strip().strip('\n').strip('\r')
    print(cleaned_line_of_mbit_data)

    # get variable name and value
    if ":" in cleaned_line_of_mbit_data:
        variable, value = get_variable_and_value(cleaned_line_of_mbit_data)
    else:
        print('Serial data from Micro:Bit not in correct format')
        
        # process the data and post to thingspeak
        if variable in API_FIELDS:
            field = API_FIELDS[variable]
            
            # prep the data in json to do a post request
            json_data = {'api_key':WRITE_API_KEY, field:value}
            
            # do a post request to api url
            response = requests.post(POST_URL, data=json_data)
            if response.status_code == 200:
                print(f"Status code {response.status_code}, Sent data {json_data}")
            else:
                print(f"Status code {response.status_code}, Did not send data")
        else:
            print('Data received from Micro:Bit out of scope / not needed')
