import json

with open('config.json', 'r') as f:
    config = json.load(f)

#edit the data
print(config["yelp-api"]["CLIENT-ID"])
print(config["yelp-api"]["ClIENT-SECRET"])
print(config["yelp-api"]["CLIENT-SECRET"])