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

def repost_happymail_pcmax():
  adult_flag = True
  genre_flag = setting.genre_flag
  name = "ももか"
  title = "25歳年上の夫と2年営みがありません.."
  text = """初めまして( ^ω^ )
都内在住で専業主婦をしている26歳のももかです♪
結婚して2年が経つんですけど、毎日楽しく何の不自由もなく
過ごせてます◎

でも１つだけ悩みがあって夫の年齢が25個上で体力が無くて結婚してから全く夜の営みがないことです...
まだ26歳だしこのまま女として終わっていくのはすごく悲しいです。。。
だから夫は仕事の関係で毎月、1ヶ月のうち1週間出張に行くのでそのタイミングで長期的に会えるせふれさんを1人探そうと思って登録してみました！！

年上も年下も大好きだし、容姿とかも特に気にしないんですけど秘密の関係を
続けられる人だと嬉しいです♪
最後に簡単にプロフィールを載せておくので気になった方はぜひメッセージください( ^ω^ )

＝プロフィール＝
・26歳
・156cm/47kg/Gカップ
・最近サウナにハマってて、時間ができたらよく行ってます♪"""

  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  h_w = func.get_windowhandle("happymail", name)
  p_w = ""

  try:   
    happymail.re_post(name, h_w, driver, title, text, adult_flag, genre_flag)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  # try:
  #   pcmax.re_post(name, p_w, driver)
  # except Exception as e:
  #   print('=== エラー内容 ===')
  #   print(traceback.format_exc())
  driver.quit()
  return True

if __name__ == '__main__':
  repost_happymail_pcmax()