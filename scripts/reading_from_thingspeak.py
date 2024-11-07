import time
import requests
import base64

def test_post(count):
    POST_URL = "https://api.thingspeak.com/update.json"
    json_data = {'api_key':"VPS1BCH04YUJMUBJ", "field1":count}
    response = requests.post(POST_URL, data=json_data)
    print(f"posting status {response.status_code}")

def get_request(url):
    # return json data if code 200, else none
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Status code {response.status_code}, Received data")
        return response
    else:
        print(f"Status code {response.status_code}, Did not receive data")
        return None
    
CHANNEL_ID = 2730808
READ_API_KEY_BASE_64 = "MzgyS09XQTJPODM1OUhLSg=="
READ_API_KEY = base64.b64decode(READ_API_KEY_BASE_64).decode()
API_FIELDS = {"cycle":"field1", 'slouch':"field2", "light":"field3"}

# https://api.thingspeak.com/channels/9/fields/2/last.csv?api_key=E52AWRAV1RSXQQJW&status=true

# cycle
GET_URL_FIELD_1 = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/1/last.json?api_key={READ_API_KEY}&status=true"

# slouch
GET_URL_FIELD_2 = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/2/last.json?api_key={READ_API_KEY}&status=true"

# light
GET_URL_FIELD_3 = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/3/last.json?api_key={READ_API_KEY}&status=true"

# start reading data from thingspeak
count = 0
while True:

    count += 1
    test_post(count)
    
    # get json data
    # field_1 = get_request(GET_URL_FIELD_1).json()
    # print(type(field_1))
    # field_2 = get_request(GET_URL_FIELD_2).json()
    # print(type(field_2))
    field_3 = get_request(GET_URL_FIELD_3).json()
    print(field_3)
    
    # check is data is valid

    # {'created_at': '2024-11-07T04:58:14Z', 'entry_id': 4, 'field1': '45', 'status': None}
    # -1

    # if type(field_1) is not dict:
    #     print('No last value detected for field 1')
    # else:
    #     print(field_1["field1"])
    
    # if type(field_2) is not dict:
    #     print('No last value detected for field 2')
    # else:
    #     print(field_2["field2"])

    if type(field_3) is not dict:
        print('No last value detected for field 3')
    else:
        print(field_3["field3"])

    # process data

    # append all fields to html file together
    

    
