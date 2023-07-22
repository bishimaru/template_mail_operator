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

mailaddress = 'yuko414510@gmail.com'
password = 'sytrqfpjwciqzzzo'
text = """メアド交換ありがとうございます♪
やりとりしていた『ゆうこ』です(*´∇｀*)

あ！会うときのお話しをしますね！！

ホテルデートからはじめて仲良くなりたいんですけど、1度きりの関係になってしまうのだけは絶対に嫌なんです（ ;  ; ）
だから最初会うときはホテル代とは別に「私たち2人と会って２万円ずつ」か、いきなり３Pが不安だったら「私1人とだけ会って２万円」をお願いしますm(_ _)m

最初にお願いしたおかねは2回目から1万円ずつお返ししていけば3回はお約束できるし、そこで相性会ったら私たちの共用のせふれさんに是非なってほしいです(*´∇｀*)

初めて会うときは私たち2人か私だけのどっちがいいですか？？"""
func.send_conditional(user_name, user_address, mailaddress, password, text)