from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import json


class GettingMindSphereToken(object):

    def __init__(self):
        self.mindsphere_token = ''

    def steal_token(self, login, password, head=False):
        options = ChromeOptions()
        options.add_argument("disable-extensions")
        options.add_argument("incognito")
        if head:
            options.add_argument("headless")
        # path_to_chrome = r'.\chromedriver.exe'
        path_to_chrome = r'./chromedriver'
        self.browser = Chrome(path_to_chrome, chrome_options=options)
        self.browser.get('https://academy2.eu1.mindsphere.io')
        self.wait_until_css_element_object_found('#login-button')
        self.browser.find_element_by_css_selector('#emailaddress').send_keys(login)
        self.browser.find_element_by_css_selector('#passLogin').send_keys(password)
        self.browser.find_element_by_css_selector('#login-button').submit()
        self.wait_until_css_element_object_found('[title= "Token App"]')
        self.browser.find_element_by_css_selector('[title= "Token App"]').click()
        self.wait_until_css_element_object_found('#myInput')
        self.mindsphere_token = self.browser.find_element_by_css_selector('#myInput').text
        print(self.mindsphere_token)
        self.browser.quit()

    def wait_until_css_element_object_found(self, css_param, wait_time=10):
        wait = WebDriverWait(self.browser, wait_time)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_param)))


if __name__ == '__main__':
    hint = GettingMindSphereToken()
    with open(Path('hidden/credential.json'), 'r') as reading_file:
        my_credentials = json.loads(reading_file.read())
    hint.steal_token(my_credentials['user_name'], my_credentials['password'])
