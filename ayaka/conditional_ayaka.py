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

mailaddress = 'ayaka414510@gmail.com'
password = 'ksjdpppibyvhfcts'
text = """あやかです(o^^o)
メアド交換ありがとうございます！

まず会う時のお話をさせてもらいたいんですが、ホテル代と別に2〜3万円を今後のホテル代として預けてもらいたいですm(__)m
1度きりの出会いになってしまうことがあると聞いて不安なので(>_<)

ホテル代使い切った時にはそんな心配もないし、仕事終わりにお家でゆっくり会ったりもいいかなって思ってます( ´ ▽ ` )

それでも良ければお返事もらえませんか？？
  """
func.send_conditional(user_name, user_address, mailaddress, password, text)