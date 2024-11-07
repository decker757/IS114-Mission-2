import time
import requests
import base64
import keyboard

def get_request(url):
    # return json data if code 200, else none
    response = requests.get(url)
    if response.status_code == '200':
        print(f"Status code {response.status_code}")
        return response
    else:
        print(f"Status code {response.status_code}")
        return None
    
CHANNEL_ID = XXX
READ_API_KEY_BASE_64 = "XXXXXXXXXXXXXXXXXX"
READ_API_KEY = base64.b64decode(WRITE_API_KEY_BASE_64).decode()
API_FIELDS = {"cycle":"field1", 'slouch':"field2", "light":"field3", "availability":"field4"}

# cycle
GET_URL_FIELD_1 = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/1/last.json"

# slouch
GET_URL_FIELD_2 = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/2/last.json"

# light
GET_URL_FIELD_3 = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/3/last.json"

# availability
GET_URL_FIELD_4 = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/4/last.json"

# start reading data from thingspeak
print("Press 'q' to exit the loop.")
while True:
    
    # get json data
    field_1 = get_request(GET_URL_FIELD_1)
    field_2 = get_request(GET_URL_FIELD_2)
    field_3 = get_request(GET_URL_FIELD_3)
    field_4 = get_request(GET_URL_FIELD_4)
    
    # check is data is valid

    # process data

    # append all fields to html file together
    
    # Check if 'q' is pressed
    if keyboard.is_pressed('q'):
        print("Exiting loop.")
        break
    
