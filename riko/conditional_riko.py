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

mailaddress = 'riko414510@gmail.com'
password = 'cygsbqgxhxcqtfyy'

text = """りこです♪
無事に連絡先交換できてよかったです(*´∇｀*)
これからよろしくお願いします♪

あっあと会う時にお願いなんですけど、最初はホテル代と別に2万円を預けて欲しいです！
1度きりで会えなくなるってことがこういう出会いではあるらしいので（ ;  ; ）

次会う時から1万円づつお返ししていけば最低でも3回は会えるし、そこで相性合うようなら長期的な関係になれたら嬉しいです♪( ´θ｀)ノ

それでも大丈夫ならお返事もらえませんか？？"""
func.send_conditional(user_name, user_address, mailaddress, password, text)