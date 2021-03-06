from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import os
import json


class GettingMindSphereToken(object):

    def __init__(self, headless=False):
        self.mindsphere_token = ''
        options = ChromeOptions()
        options.add_argument("disable-extensions")
        options.add_argument("incognito")
        if headless:
            options.add_argument("headless")
        if os.name == 'nt':
            path_to_chrome = str(Path('./chromedriver.exe').relative_to('.'))
        else:
            path_to_chrome = str(Path('./chromedriver').absolute())
        self.browser = Chrome(path_to_chrome, chrome_options=options)

    def logging_in(self, login, password):
        self.browser.get('https://academy2.eu1.mindsphere.io')
        self.wait_until_css_element_object_found('#login-button')
        self.browser.find_element_by_css_selector('#emailaddress').send_keys(login)
        self.browser.find_element_by_css_selector('#passLogin').send_keys(password)
        self.browser.find_element_by_css_selector('#login-button').submit()

    def steal_token(self, token_app_name, token_json):
        self.wait_until_css_element_object_found('[title= "' + token_app_name + '"]')
        self.browser.find_element_by_css_selector('[title= "' + token_app_name + '"]').click()
        self.wait_until_css_element_object_found('#myInput')
        self.mindsphere_token = self.browser.find_element_by_css_selector('#myInput').text
        print(self.mindsphere_token)
        token_dict = {'auth_token': self.mindsphere_token}
        with open(token_json, 'w') as out:
            out.write(json.dumps(token_dict, indent=4) + '\n')
        self.browser.quit()

    def wait_until_css_element_object_found(self, css_param, wait_time=10):
        wait = WebDriverWait(self.browser, wait_time)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_param)))


if __name__ == '__main__':
    credential_file = Path('hidden/credential.json')
    fetching_token = GettingMindSphereToken()
    with open(credential_file, 'r') as reading_file:
        my_credentials = json.loads(reading_file.read())
    fetching_token.logging_in(my_credentials['user_name'], my_credentials['password'])
    # fetching_token.steal_token('Token App', Path('hidden/token.json'))
