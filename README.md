# SHOUT
`A User-Friendly web application powered by the Yelp Fusion API.`

Live Demo and Overview: https://www.youtube.com/watch?v=1B-GNInJWo0&t=8s
This app generates nearby restaurant suggestions driven by user choices in an interactive wizard. The main django app is located in `app/shout`.
![main image](https://github.com/andrewjton/SHOUT/blob/master/readme_imgs/main.png)



------------------------------------------------------------------------


## Overview of Features
1. HTML 5 Geolocation
2. Google maps Embed and integration
3. Image-based User selection
4. Organized User Data
5. Security 
6. Interactive Mobile Responsive Design


------------------------------------------------------------------------


## Overview of System Design
![system-design-img](https://github.com/andrewjton/SHOUT/blob/master/readme_imgs/system-design.png)


------------------------------------------------------------------------


# Features Described in Depth

### Geolocation and Google Maps embedded
![system-design-img](https://github.com/andrewjton/SHOUT/blob/master/readme_imgs/maps.png)
I integrated google maps' geolocation API that comes with HTML5. This was a surprisingly trivial task and the javascript integrated fairly smoothly.

### Frontend Features
- Wizard for navigation (javascript library)
- Image based User selection (javascript library)
![img-selection-img](https://github.com/andrewjton/SHOUT/blob/master/readme_imgs/image-based.png)

I designed the frontend to be very user-friendly. Users navigate through the javascript form wizard and enter their preferences. The location is automatically entered for them and they can select various images that represent their food preferences for the evening.


### Backend Features
- Django (Python Web Framework)
- YELP rest API (Python script)
- Jinja (templating language that follows the DRY principle)
- SQLite database
The backend is developed using the Django Web frameworks and user data is stored in a SQLite database. I rendered the front end by writing templates in Jinja. To generate the search results, I wrote several JQuery/Ajax scripts that asynchronously call a REST api (python) that communicates with the Yelp Fusion API. These results are rendered using the Jinja templating language.
![results-img](https://github.com/andrewjton/SHOUT/blob/master/readme_imgs/results.png)

### User Data and Security
Each user interaction with the webpage is stored in a SQLite databse. Their food preferences, location, and personal information (optional) are stored, because it is very useful for businesses. The reality of the internet is that most of our information is repackaged and sold to marketing and analytics agencies. 

User privacy is extremely important, so entering in identity and e-mail data is entirely optional and the transaction data is protected in the database. Django has `form sanitization` features which protect this application from `SQL-injection` attacks which could corrupt db data or steal it. Another feature is `CSRF protection` for the views that I wrote. This prevents `cross site scripting` attacks.

![final-img](https://github.com/andrewjton/SHOUT/blob/master/readme_imgs/final.png)
