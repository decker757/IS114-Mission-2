import time
import requests
import base64
import json

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

def format_fields_json(field1list, field2list):
    # returns a list of dicts, to be dumped int json file
    # len of field1list is the same as len of field2list
    # field1 is cycle, field2 is slouch
    r_lis = []
    for i in range(len(field2list)):
        data_to_save = {"cycle": field1list[i]["field1"], "slouch": field2list[i]["field2"], "timestamp": field2list[i]["created_at"]}
        r_lis.append(data_to_save)
    return r_lis

CHANNEL_ID = 2730808
READ_API_KEY_BASE_64 = "MzgyS09XQTJPODM1OUhLSg=="
READ_API_KEY = base64.b64decode(READ_API_KEY_BASE_64).decode()
API_FIELDS = {"cycle":"field1", 'slouch':"field2"}

# cycle
GET_URL_FIELD_1 = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/1/last.json?api_key={READ_API_KEY}&status=true"
# slouch
GET_URL_FIELD_2 = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/2/last.json?api_key={READ_API_KEY}&status=true"
        

all_field1 = []
all_field2 = []

# start reading data from thingspeak
while True:
    
    # get json data
    field1 = get_request(GET_URL_FIELD_1)
    field2 = get_request(GET_URL_FIELD_2)

    # check is data is valid and process
    # {'created_at': '2024-11-07T04:58:14Z', 'entry_id': 4, 'field1': '45', 'status': None}

    if field1 is not None:
        # field 1 is dict
        all_field1.append(field1)
    else:
        #field1 is none
        print('Unable to read field1 from thingspeak')

    if field2 is not None:
        # field2 is dict
        all_field2.append(field2)
    else:
        # field2 is none
        print('Unable to read field2 from thingspeak')
    
    dumpthis = format_fields_json(all_field1, all_field2)
    
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(dumpthis, f)

    # the javascript in the html file will read from this json file every 5 seconds
    time.sleep(20)
