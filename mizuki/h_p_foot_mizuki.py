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
from widget import pcmax, happymail, func
from selenium.webdriver.support.ui import WebDriverWait
import setting
import traceback
from datetime import timedelta


def h_p_foot(cnt):
  name = "みづき"
  return_foot_message = """足跡みてメッセージしちゃいました♪♪
美月（みづき）と言います。
脱毛サロンのエステティシャンをしています。

おっとりとした性格で、癒し系だねとよく言われるんですが、
けっこう優しく責めるのが好きで...VIOの施術をしている時とか我慢している男の人を興奮しちゃってます(>_<)

仕事は仕事としてちゃんとやるので、問題になったことはないですが、施術が終わって頑張った後のお客様を見てるとつい「ヨシヨシ」したくなっちゃいます・・・実際はお疲れ様でしたと言うだけですが笑

仕事に支障が出る前に、プライベートであ◯こを攻めたりとか、ヨシヨシできるせふれさんが欲しいです。
こう言うものありかも？って思ってくれたらお返事お待ちしてますヽ(^o^)"""
  relative_path = os.path.join(setting.BASE_DIR, setting.mizuki_picture_path)
  h_return_foot_img = relative_path
  p_return_foot_img = ""
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  h_w = func.get_windowhandle("happymail", name)
  # p_w = func.get_windowhandle("pcmax", name)
  p_w = ""

  try:   
    func.h_p_return_footprint(name, h_w, p_w, driver, return_foot_message, cnt, h_return_foot_img, p_return_foot_img)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  driver.quit()
  return True
if __name__ == '__main__':
  if len(sys.argv) < 2:
    cnt = 20
  else:
    cnt = int(sys.argv[1])
  h_p_foot(cnt)