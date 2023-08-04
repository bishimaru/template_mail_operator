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

mailaddress = 'yua414510@gmail.com'
password = 'puzncjcobqoppyvw'
text = """アドレス交換した『ゆあ』です！
これから沢山お会いして行けたら嬉しいです♫

私たち、ホテルデートから始めて行けたらって思ってるんですけど、その時かぎりの関係とには全く興味無くて長期的な夜の専属パートナーになってくれる方を求めてるので、最初にホテル代とは別に『私たち2人と会って2万円づつ』か『私1人とだけ会って2万円』をお願いします(^ ^)


もらったお金は次回会う時のホテル代とか３人で会うために必要なものに当てていけたらって思ってます♫

最初に会うときは私たち2人とか私だけのどっちがいいですか？？"""
func.send_conditional(user_name, user_address, mailaddress, password, text)