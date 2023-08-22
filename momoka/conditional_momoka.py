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

mailaddress = 'momoka414510@gmail.com'
password = 'uhmoqgczqtdpzxmx'

text = """メアド交換したももかです♪
早速メール送っちゃいました( ^ω^ )

色んな人からメッセージ来てたんですけど、直感でこの人だ！
って思ってメッセしました♪
これから長く関係を続けていけると嬉しいです🌟

私は長期的な出会いを探しているので、最初に会う時は
ホテル代と別に2万円お願いできると嬉しいです♪
最低でも3回は会うためのホテル代としてお預かりして、
もちろんホテル代を使い切ったあとは割り勘で大丈夫だし、
私のお家に泊まったりとかもOKです（ ;  ; ）
なのでこの条件でも良かったらお返事欲しいです!"""
func.send_conditional(user_name, user_address, mailaddress, password, text)