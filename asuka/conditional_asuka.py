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

mailaddress = 'asuka414510@gmail.com'
password = 'ffmogbvrtzkvnqre'
text = """良かった♪
これから宜しくお願いします( ˊ̱˂˃ˋ̱ )

お会いする時のお願いがあるんですけど、
私もゆかも初めてのセフレ募集で色々と不安で...

１度きりの関係にならないように、先ずは私とだけ会ってホテル代と別に２万円か2人と会って2万円づつをお願いしたいです(>_<)

次回からはお金とかは勿論いらないですし、ホテル代とかも私たちが出していくので安心してください♪

お願いが大丈夫そうならお返事くださいね(● ˃̶͈̀ロ˂̶͈́)੭ꠥ⁾⁾
  """
func.send_conditional(user_name, user_address, mailaddress, password, text)