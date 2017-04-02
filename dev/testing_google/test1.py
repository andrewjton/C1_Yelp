import json
import googlemaps
from datetime import datetime

with open('../config.json', 'r') as f:
    config = json.load(f)
key = config["maps-api"]["key"]
gmaps = googlemaps.Client(key=key)

# Geocoding an address
print("Obtaining Geocode from address...")
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
print(geocode_result)

# Look up an address with reverse geocoding
print("Testing reverse Geocode...")
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
print(reverse_geocode_result)

# Request directions via public transit
now = datetime.now()

print("Obtaining Directions from address...")
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
#directions = json.loads(directions_result)
print(directions_result)

#prettifying json

#directions = []
#for i in directions_result:
#	directions.append(json.loads(str(i)))
	
#print(json.dumps(directions, indent=4, sort_keys=True))