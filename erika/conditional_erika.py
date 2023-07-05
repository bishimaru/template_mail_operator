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

mailaddress = 'k.erika414510@gmail.com'
# password = 'afhbvdtdsvkvkvle'
password = 'mqaopcxgtkkhjafw'

text = """えりかです！！
メアド交換ありがとうございます♪
これから関係が長く続けれるのが理想です♪( ´θ｀)ノ

あといきなりなんですけど、やっぱり1回限りの関係とかワンナイトで終わっちゃうのがすごく不安なので最初に会う時に最低3回は会うためのホテル代として最初のホテル代と別に2〜3万円をお願いできると嬉しいです（ ;  ; ）

それをホテル代として使い切ったあとは割り勘でも大丈夫だし、お家で会うのもいいなって思ってます◎

それでもよければお返事もらえませんか？？
  """
func.send_conditional(user_name, user_address, mailaddress, password, text)