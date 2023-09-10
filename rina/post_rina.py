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
  title = "初めてのセフさんになって貰えませんか？"
  text = """初めまして(｡･ω･)ﾉﾞ 

プロフィール見ていただきありがとうございますー！
都内の総合病院で看護師として働いているりなって言います！

忙しいですが充実した日々を送っています、相手の気持ちに寄り添える看護師にと、頑張っているところです...！
月に4回ほど夜勤があり、お休みは不定期になります。

【休日の過ごし方】

お休みの日はお友達とお出かけしたり、好きなアーティストのライブに行ったりしてます！フェスに行くのも好きですっ

何も予定が無かったらNetflixでアニメとかも観たりしてます！ヒロアカ、ブルーロック、ドクターストーンを最近は見ました！

フェス、アニメ・漫画・ゲーム等含め幅広い好きがあります...!

色々なことに興味があり、経験がないこともまずはやってみたいと考える性格なので、共通の趣味でなくとも一緒に楽しむことができたらと考えています。
嬉しいことも楽しいことも、悲しいことも嫌なことも共有できるような関係性が理想です...！

一方で、お互いに快適な距離感を維持したいとも思っているので、無理に全部を知りたいとは思っていません誠実な関係性を築けたらいいなって思っています(⁠｡⁠•̀⁠ᴗ⁠-⁠)⁠

こんな私との関係に興味があるよーって方は連絡貰えたら嬉しいです！"""
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