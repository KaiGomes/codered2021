import googlemaps
import json
import requests
from requests.api import request
from requests.models import Response
from config import API_KEY
from urllib.parse import urlencode


gmaps = googlemaps.Client(key = API_KEY)
origin = "106 Zephyr Bend Place, The Woodlands, TX"
dest = "4800 Calhoun Rd, Houston, TX"

# data_type = 'json'
# base_geocode_url = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
# parameters = {
#     'key' : API_KEY,
#     'address' : address
# }
# url_params = urlencode(parameters)
# url = f"{base_geocode_url}?{url_params}" #url is equal to base_geocode_url + ? + urlparams
# print (url)

def extract_lat_long(address, data_type = 'json'):
    base_geocode_url = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    parameters = {
        "address" : address,
        "key" : API_KEY
    }
    url_params = urlencode(parameters)
    url = f"{base_geocode_url}?{url_params}"
    print(url)
    r = requests.get(url)
    if r.status_code not in range (200,299):
        return {}
    return r.json()
    
def extract_directions(origin, dest, data_type = 'json'):
    base_geocode_url = f"https://maps.googleapis.com/maps/api/directions/{data_type}"
    parameters = {
        "origin" : origin,
        "destination" : dest,
        "alternatives" : "true",
        "key" : API_KEY
    }
    url_params = urlencode(parameters)
    url = f"{base_geocode_url}?{url_params}"
    print(url)
    r = requests.get(url)
    if r.status_code not in range (200,299):
        return {}
    return r.json()


#print (extract_lat_long(origin))
#print (extract_lat_long(dest))
output = extract_directions(origin, dest)
print(len(output["routes"]))

with open("output.json", "w") as file :
    file.write(json.dumps(output, indent=4))