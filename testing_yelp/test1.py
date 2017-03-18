from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key=YOUR_CONSUMER_KEY,
    consumer_secret=YOUR_CONSUMER_SECRET,
    token=h4rDav15vfplgH2c-MrE3w,
    token_secret=cKvSE3Sh2p7yUhvYPCX3KQ5Li7hUUlms9H8Ou8uMrcQ89vUjDouLH2LlRbGt2wnf
)

client = Client(auth)