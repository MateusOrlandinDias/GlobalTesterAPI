import json
import os

def InitAllSettings():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    
    print('> Init All Settings done. Config Available.')
    return config