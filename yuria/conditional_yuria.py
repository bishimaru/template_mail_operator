import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import func
import traceback
from email.mime.text import MIMEText
from email.utils import formatdate
if len(sys.argv) < 3:
    print("引数を正しく入力してください")
    user_name = ""
    user_address = ""
else:
  user_name = str(sys.argv[2])
  user_address = str(sys.argv[1])

mailaddress = 'k.yuria.0722@gmail.com'
password = 'mbvjzdrerdljzbls'
text = """メアド交換ありがとうございます(^ ^)
ゆりあです♪

お互いに都合が良いときに人肌を埋めれるような関係が理想です！

あと最初会う時はホテルデートから始めたいんですけど、1回きりの出会いっていうのが私としては絶対嫌なのでホテル代と別に2万円を預けてもらいたいですm(_ _)m
2回目から5千円づつ返していけば最低でも4回は会えるし、その頃にはお互いのことを理解できてると思います♪"""
func.send_conditional(user_name, user_address, mailaddress, password, text)