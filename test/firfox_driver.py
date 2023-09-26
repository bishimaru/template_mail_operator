from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import func

# options = webdriver.FirefoxOptions()

# options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1")
# options.add_argument("--no-sandbox")

# driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))

# # Googleを開く
# driver.set_window_size(456, 912)
# driver.get('https://www.google.com/')
driver = func.get_firefox_driver()
driver.get('https://www.google.com/')






