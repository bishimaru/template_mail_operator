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
  genre_flag_pcmax = setting.genre_flag_pcmax
  name = "りな"
  title = "ゲームとお酒が好きな看護師です！20代のうちに楽しみたい♪"
  text = """初めまして！看護師のりなです♪

普段は仕事に追われて休みの日もあんまり出会いの場とか行かないですし、なかなか出会いがないんですよね。。。

なのでせっかくの20代を楽しみたいと思ってこちらに登録してみました！

趣味はゲームで、最近はマイクラにハマっています٩(*´︶`*)۶
ゲームの話とかもできる人だと嬉しいです！

ゲーム以外だとNetflixで韓国ドラマとか色々観たりしていてどちらかというとインドア派です〜！

今は仕事に専念したい気持ちがあるので、恋人というよりせふれ関係になれる人が欲しいです！優しくて、一緒にいて楽しい人が好きです。
でもいきなりそんな関係になるのは難しいと思うので、ゆっくり信頼関係を深められたらと思います。

こんな私とセフの関係に興味あったらメッセージくれたら嬉しいです！"""
  options = Options()
  options.add_argument('--headless')
  options.add_argument("--no-sandbox")
  options.add_argument("--remote-debugging-port=9222")
  options.add_experimental_option("detach", True)
  service = Service(executable_path="./chromedriver")
  driver = webdriver.Chrome(service=service, options=options)
  h_w = func.get_windowhandle("happymail", name)
  p_w = func.get_windowhandle("pcmax", name)
  try:   
    happymail.re_post(name, h_w, driver, title, text, adult_flag, genre_flag)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  try:
    pcmax.re_post(name, p_w, driver, genre_flag_pcmax)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  driver.quit()

if __name__ == '__main__':
  repost_happymail_pcmax()