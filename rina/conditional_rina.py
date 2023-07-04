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
  user_name = str(sys.argv[1])
  user_address = str(sys.argv[2])

mailaddress = 'k.rina414510@gmail.com'
password = 'afbqhyngnoxigont'
text = """りなです。
アドレス交換ありがとうございます♪

会うにあたってお願いがありますm(_ _)m
お互い安心できるように、信頼関係が大切だと思っています。だから最初はホテル代と別に2万円預けて欲しいです！

体の関係だけでいなくなるのは嫌なので、2回目以降は預かったお金を5000円ずつ返していけば4回は会えますし長期的な関係を築くことができれば、お互いにとってよりよいものになると思います。

もしそのお願いが大丈夫であれば、お返事もらえますか？"""
func.send_conditional(user_name, user_address, mailaddress, password, text)