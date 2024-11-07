import time
import requests
import base64


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

def get_variable_and_value(string):
    # returns variable value pair if the string from microbit is valid
    try:
        first, second = string.split(':')
        return first, second
    except:
        print('Serial data not in correct format')
        return None
        

field1uniq = []
field2uniq = []
field3uniq = []
# initialise serial connection

print('out')

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

    
    lines_for_3 = [f"<tr>{line[field3]}</tr>" for line in field3uniq]
    lines_for_2 = [f"<tr>{line[field2]}</tr>" for line in field2uniq]
    lines_for_1 = [f"<tr>{line[field1]}</tr>" for line in field1uniq]
    print(lines_for_3)
    print(lines_for_2)
    print(lines_for_1)

    # append all fields to html file together
    time.sleep(30)