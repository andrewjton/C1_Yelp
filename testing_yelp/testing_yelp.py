from yelp_fusion_api import *

#query_api("bars", "San Francisco")

bearer_token = obtain_bearer_token(API_HOST, TOKEN_PATH)

print(search(bearer_token, "bars", "150.644", "-34.397"))