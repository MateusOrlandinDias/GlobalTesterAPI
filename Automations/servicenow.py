from Automations import config as cfg
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class ServiceNow:
    def __init__(self):
        self.config = cfg.InitAllSettings()
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)
    
    def kill_browser(self):
        self.driver.quit()

    def login(self):
        self.driver.get("")