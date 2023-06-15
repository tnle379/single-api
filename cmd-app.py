import argparse
import requests
import json
import os
import validators
from jsonschema import validate

#---------------------------------
# setting up arguments
#---------------------------------

# validate file type and file existence
def validate_file_from_argument(fileName: str, fileType: str):
    ext = os.path.splitext(fileName)[1][1:]
    if ext != fileType:
        parser.error(f"Wrong file type, requires a .json file.")
    
    if not os.path.exists(fileName):
        parser.error(f"File {fileName} does not seem to exist")

    return fileName

#validate url format
def validate_url(url):
    if not validators.url(url):
        parser.error(f"Invalid url format. Check -h or --help.")
    else:
        return url

parser = argparse.ArgumentParser()
ARGUMENT_TYPE_CHOICES=('GET','POST')

parser.add_argument('-u', '--url', dest='url', help='Please provide the url of site. Ex: http://localhost:8000, http://127.0.0.1:8000', required=True, type=lambda u:validate_url(url=u))
parser.add_argument('-t', '--type', dest='type', help=f'Provide type of request. Ex: {ARGUMENT_TYPE_CHOICES}.', choices=ARGUMENT_TYPE_CHOICES, required=True) 
parser.add_argument('-f', '--filename', dest='filename', help='If POST request, please provide a .json file. Please check the README file for the accepted formatting of the .json file.', type=lambda s:validate_file_from_argument(fileName=s, fileType='json'))

args = parser.parse_args()
#---------------------------------
#
#---------------------------------

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "type": {"type": "string"},
        "description":{"type":"string"},
        "date": {"type": "string"},
    },
    "required": ["name"],
    "required": ["type"],
    "required": ["description"],
    "required": ["date"],
}

# validate json schema
def validate_json_schema(data: dict):
    try:
        data_list = data['submissions'] 
        for json_data in data_list:
            validate(instance=json_data, schema=schema)
        return True
    except KeyError as e:
        raise Exception('Invalid JSON format. Please check README for examples.')

    

# read json file to json
def read_file_to_json(filename: str):
    with open(filename) as json_file:
        data = json.load(json_file)

    if validate_json_schema(data):
        return data

# send GET request
def get_request(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()

        return response.text
    
    except requests.exceptions.ConnectionError as e:
        raise Exception("Connection error!! You might have not started your API server.")

# send POST request
def post_request(url: str, filename: str):
    body = read_file_to_json(filename=filename)
    try:
        response = requests.post(url=url, json=body)
        response.raise_for_status()

        return response.text
    
    except requests.exceptions.ConnectionError as e:
        raise Exception("Connection error!! You might have not started your API server.")

# make connection with API to get objects
def get_objects(type: str, url: str):
    body = None
    if type == 'GET':
        body = get_request(url=url)
    
    elif type == 'POST':
        if args.filename is None:
            parser.error("POST request requires a --filename option. Check -h or --help.")
        body = post_request(url=url, filename = args.filename)

    data = json.loads(body)["results"]
    return sort_objects_by_date(data_list=data)

# sort the dictionary based on "date" key
def sort_objects_by_date(data_list: list):
    data_list.sort(key=lambda item:item['date'], reverse=True)
    return data_list

def main():
    sorted_data = get_objects(type=args.type, url=args.url)
    print(f'{sorted_data}')

main()