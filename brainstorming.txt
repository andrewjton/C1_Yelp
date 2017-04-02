sample query return!

{'price': '$$$', 'distance': 3353.1287697519997, 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/RLiIhIbsrPkl_kl9bwfQUA/o.jpg', 'name': 'The Saratoga', 'display_phone': '(415) 932-6464', 'url': 'https://www.yelp.com/biz/the-saratoga-san-francisco?adjust_creative=h4rDav15vfplgH2c-MrE3w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=h4rDav15vfplgH2c-MrE3w', 'review_count': 76, 'location': {'zip_code': '94109', 'country': 'US', 'display_address': ['1000 Larkin St', 'San Francisco, CA 94109'], 'address1': '1000 Larkin St', 'city': 'San Francisco', 'address3': '', 'state': 'CA', 'address2': ''}, 'transactions': [], 'rating': 4.0, 'is_closed': False, 'id': 'the-saratoga-san-francisco', 'categories': [{'title': 'American (New)', 'alias': 'newamerican'}, {'title': 'Bars', 'alias': 'bars'}], 'phone': '+14159326464', 'coordinates': {'latitude': 37.787329020702, 'longitude': -122.418082801733}}, 

{'price': '$$', 'distance': 3289.723348696, 'image_url': 'https://s3-media3.fl.yelpcdn.com/bphoto/Vpxb8aKk6uGmrnIo5XlQDw/o.jpg', 'name': 'Rum&Sugar', 'display_phone': '(415) 913-7949', 'url': 'https://www.yelp.com/biz/rum-and-sugar-san-francisco?adjust_creative=h4rDav15vfplgH2c-MrE3w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=h4rDav15vfplgH2c-MrE3w', 'review_count': 27, 'location': {'zip_code': '94109', 'country': 'US', 'display_address': ['823 Geary St', 'San Francisco, CA 94109'], 'address1': '823 Geary St', 'city': 'San Francisco', 'address3': '', 'state': 'CA', 'address2': None}, 'transactions': [], 'rating': 4.5, 'is_closed': False, 'id': 'rum-and-sugar-san-francisco', 'categories': [{'title': 'Bars', 'alias': 'bars'}], 'phone': '+14159137949', 'coordinates': {'latitude': 37.7861178, 'longitude': -122.4169129}}, 

{'price': '$$', 'distance': 3936.74175856, 'image_url': 'https://s3-media2.fl.yelpcdn.com/bphoto/BqaSyScp9GV1Nqt8tNw3Lg/o.jpg', 'name': 'Coin-Op Game Room', 'display_phone': '(628) 444-3277', 'url': 'https://www.yelp.com/biz/coin-op-game-room-san-francisco-2?adjust_creative=h4rDav15vfplgH2c-MrE3w&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=h4rDav15vfplgH2c-MrE3w', 'review_count': 93, 'location': {'zip_code': '94107', 'country': 'US', 'display_address': ['508 4th St', 'San Francisco, CA 94107'], 'address1': '508 4th St', 'city': 'San Francisco', 'address3': '', 'state': 'CA', 'address2': ''}, 'transactions': [], 'rating': 4.0, 'is_closed': False, 'id': 'coin-op-game-room-san-francisco-2', 'categories': [{'title': 'Pizza', 'alias': 'pizza'}, {'title': 'Arcades', 'alias': 'arcades'}, {'title': 'Cocktail Bars', 'alias': 'cocktailbars'}], 'phone': '+16284443277', 'coordinates': {'latitude': 37.7791938781738, 'longitude': -122.398078918457}}



categories: restaurants, 

soup


Search QUERY
-categories ()
-radius (depends on if walking/driving - can integrate with google API later!)
-location (address, neighborhood, city, state or zip) OR long/lat (obtained from HTML5 location??)
-price (1-4, user generated)
-search (can just do categories for this)
-attributes (deals, "hot_and_new")

0. obtain user location, and preferences
1. Load up 20 restaurants (close by) -- OR -- have 20 stock images! representative of different types of cuisine
2. Ask user to choose additional preferences [cost, additional keywords, deals, etc.]
3. query api
4. display results on nice page & save transaction + google maps integration that shows map + shows distance of each selection

Designing Yelp-API interface
0. finishing form redirects you to next page w/ a json including all your parameters
1. next page contains a javascript ajax call to your django api which you call w/ your parameters
2. django api recieves your parameters and returns it as json
3. your page renders the json
4. ideally something renders while the execution occurs
django api: /query-yelp/keywords/price/categories/radius/location/deals
	
TODO
add more preferences to api query
error handling for no results
lat/long support for searching api
remove hard-coding for searchapi	


Features
image-based selection
HTML 5 location (use chrome!)
Google maps integration and location visualization
Wizard form
asynchronous loading (javascript and ajax)
db storage of data transactions
responsive web design
Django forms
Long/lat lookup (only...)
Yelp Fusion API 
internal rest api