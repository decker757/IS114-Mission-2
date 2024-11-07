import time
import requests
import base64

def test_post(count):
    POST_URL = "https://api.thingspeak.com/update.json"
    json_data = {'api_key':"VPS1BCH04YUJMUBJ", "field2":count}
    response = requests.post(POST_URL, data=json_data)
    print(f"posting status {response.status_code}")

def get_request(url):
    # return json data if code 200, else none
    response = requests.get(url)
    if response.status_code == 200:
        # print(f"Status code {response.status_code}, Received data")
        if response.json() == -1:
            # no last entry
            return None
        
        elif type(response.json()) == dict:
            # returns last value
            return response.json()
        
        else:
            # unknown json data
            return None
    else:
        # status code 400
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

field1uniq = []
field2uniq = []
field3uniq = []

# start reading data from thingspeak
while True:
    
    # get json data
    field1 = get_request(GET_URL_FIELD_1)
    # print(field1)
    field2 = get_request(GET_URL_FIELD_2)
    # print(field2)
    field3 = get_request(GET_URL_FIELD_3)
    # print(field3)
    
    # check is data is valid and process

    # {'created_at': '2024-11-07T04:58:14Z', 'entry_id': 4, 'field1': '45', 'status': None}

    if field1 is not None and field1 not in field1uniq:
        # field 1 is dict
        field1uniq.append(field1)
    else:
        #field1 is none
        print('Unable to read field1 from thingspeak')

    if field2 is not None and field2 not in field2uniq:
        # field2 is dict
        field2uniq.append(field2)
    else:
        # field2 is none
        print('Unable to read field1 from thingspeak')

    if field3 is not None and field3 not in field3uniq:
        # field3 is dict
        field3uniq.append(field3)
    else:
        #field3 is none
        print('Unable to read field1 from thingspeak')

    print(field3uniq)
    print(field2uniq)
    print(field1uniq)

    # append all fields to html file together
    time.sleep(30)

    
