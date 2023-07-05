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

mailaddress = 'kiriko414510@gmail.com'
password = 'wqhpalqgwdgfrdmh'
text = """メアド交換ありがとうございます○o。.

単刀直入なんですけど、やり逃げとかのリスクもあるし最初はホテル別の2万円でホテルデートしませんか？？
ストレスとか欲求不満をちゃんと解消するためにこれだけお願いしたいです(´;ω;｀)

1ヶ月間会ってみて、お互いに2ヶ月目も会いたいってなった場合はお金とか無しで関係を続行したいです♪

沢山の方とメールしても埒が明かないので、まずはこれで決めてくれる人に絞りたいなって思いますー！
お返事もらえたらまた私から連絡したいので、お返事待ってます！"""
func.send_conditional(user_name, user_address, mailaddress, password, text)