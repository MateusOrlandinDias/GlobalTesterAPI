from Automations import config as cfg
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import json

class ServiceNow:
    def __init__(self):
        self.config = cfg.InitAllSettings()
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
    
    def kill_browser(self):
        self.driver.quit()

    def login(self, username, password):
        url = 'https://gerdau.service-now.com/'

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        body = {
            'user': username,
            'password': password
        }

        response = requests.post(url, headers=headers, data=json.dumps(body))

        if response.status_code == 200:
            print('Login bem-sucedido!')
            token = response.json().get('result').get('token')
            print('Token de acesso:', token)
        else:
            print('Falha no login. Código de status HTTP:', response.status_code)
