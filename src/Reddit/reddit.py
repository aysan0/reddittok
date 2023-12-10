import requests
from utils import readRedditConfig, getAuthStateGuid

class RedditReader():


    def __init__(self):
        pass

    def Authenticate():
        config = readRedditConfig()
        client_id = config.get('redditClientID')
        secret = config.get('redditSecret')
        state = getAuthStateGuid()
        redirect_uri = 'https://localhost:8000'
        auth_endpoint = 'https://www.reddit.com/api/v1/authorize?client_id={client_id}&response_type=code&state={state}&redirect_uri={redirect_uri}&scope=read'

        response = requests.get(auth_endpoint)
        print(response)

r = RedditReader()
r.Authenticate()
