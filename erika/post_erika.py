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
  name = "えりか"
  title = "AV女優に偏見ない人。長期せふれさん！経験少ない人も◎"
  text = """〜　Profile　〜
  ・えりか/25歳/Dcup/AV女優
  ・AV女優のお仕事がない時は会員制のデリヘルで働いてます！
  ・温泉巡りが趣味でたまに連休とって体を休めています◎

  投稿見てくれてありがとうございます♪
  まずは簡単にプロフィール書いてみました！

  AVのお仕事もデリヘルのお仕事もえっちが好きで人と関わるのが大好きな私にとってはすっごく楽しいです♪( ´θ｀)ノ
  とはいえプライベートはプライベートで大事にしたいと思ってます！

  ここではプライベートを一緒に楽しめる方を探しています◎
  えっちについては私自身プロだし仕事柄プロの男優さんとか会ってきたので上手さとかそういうのは逆に気にしないですm(__)m
  その代わりに長期的な関係ってのがあまりないので、経験少ない人とどんどん相性良くなっていける関係が理想かなって思ってます！

  私の職業に偏見なくて長期的な関係でも大丈夫って方いたらメッセージもらえると嬉しいです(*ﾟ▽ﾟ*)"""

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
    happymail.re_post(name, h_w, driver, title, text, adult_flag)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  try:
    pcmax.re_post(name, p_w, driver)
  except Exception as e:
    print('=== エラー内容 ===')
    print(traceback.format_exc())
  driver.quit()
  return True

if __name__ == '__main__':
  # print(f'__name__ は{__name__}となっている。')
  repost_happymail_pcmax()