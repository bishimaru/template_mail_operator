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

mailaddress = 'meari414510@gmail.com'
password = 'mplqmtdqjdlyfsgp'

text = """メアド交換ありがとうございます♪
めありです(^ ^)

あっ最初会うときお願いがあるのでお伝えしますね！
こういう場所だとやり捨てもあるって聞いて不安なので、会うときにホテル代と別に2万円を預けてもらいたいですm(_ _)m

預けてもらった分は次から1万円づつお返しすれば最低でも3回は会えるし、そこまでしてもらえるなら長期的に会うことを考えてくれてるって安心して会えます(*´∇｀*)

返し終わった後は私のお家でまったりデートもできたらいいなって思ってます！

それでも大丈夫ならお返事もらえませんか？？"""
func.send_conditional(user_name, user_address, mailaddress, password, text)