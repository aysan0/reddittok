import os
import uuid
import json

config_path = os.path.join(os.pardir, 'config.json')
def readConfig():
    with open(config_path, 'r') as file:
        config_data = json.load(file)
        return config_data

def readRedditConfig():
    with open(config_path, 'r') as file:
        config_data = json.load(file)
        return config_data.get('reddit')

def getAuthStateGuid():
    return str(uuid.uuid4())

def readOpenAIConfig():
    with open(config_path, 'r') as file:
        config_data = json.load(file)
        return config_data.get('openai')