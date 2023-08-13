import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import func
import traceback
from email.mime.text import MIMEText
from email.utils import formatdate
# wdlnivdlmvsfzpjp
if len(sys.argv) < 3:
    print("引数を正しく入力してください")
    user_name = ""
    user_address = ""
else:
  user_name = str(sys.argv[2])
  user_address = str(sys.argv[1])

mailaddress = 'haruru414510@gmail.com'
password = 'ilvcgfuayvxglldv'

text = """メアド交換したハルです♪
無事に繋がれて良かったです✨

早速最初に会うときのお話をしていきたいんですけど、
私は長期的な出会いを探しているのと少しだけ知名度もあるので
1回限りの関係とかよりも長期的に会いたいと思ってます(T . T)

だから最初に会う時に最低3回は会うためのホテル代として最初のホテル代と別に2万円をお願いできると嬉しいです（ ;  ; ）
もちろん使い切った後は割り勘で遊んだり私のお家とかで
会えればいいなって思ってます！

もしお願い大丈夫ならお返事いただけますか？"""
func.send_conditional(user_name, user_address, mailaddress, password, text)