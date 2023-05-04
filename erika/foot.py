from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import random
import time
from selenium.webdriver.common.by import By
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import pcmax, happymail
from selenium.webdriver.support.ui import WebDriverWait


name = "えりか"
happy_windowhandle = "B3D5ED5F7BEAA4F431DEECB340773A48"
pcmax_windowhandle = "B965B0DF394F184BC5D23A57AEA3915F"
return_foot_message = """足跡からです！m(__)m
AV女優と会員制のデリヘルでお仕事しています◎

プライベートでえっちなことができるせふれさんを探しています！
仕事ではプロの男優さんとかとかと会うので上手さとかは逆に気にしないですm(__)m
その代わりに長期的な関係ってのがあまりないので、経験少ない人とどんどん相性良くなっていける関係が理想かなって思ってます♪( ´▽｀)

もし仕事に偏見なく会ってくれる人いたら連絡もらいたいです！"""

if len(sys.argv) < 2:
  cnt = 20
else:
  cnt = int(sys.argv[1])
options = Options()
options.add_argument('--headless')
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")
options.add_experimental_option("detach", True)
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service, options=options)

try:   
  happymail.return_footpoint(name,happy_windowhandle, driver, return_foot_message, cnt)
except Exception as e:
  print('error')
driver.quit()