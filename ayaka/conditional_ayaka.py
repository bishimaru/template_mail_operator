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

mailaddress = 'ayaka414510@gmail.com'
password = 'ksjdpppibyvhfcts'
text = """メアド交換ありがとうございます〜！

サイトでやり取りしたあやかですっ

いきなり驚かせてしまったらすみませんなんですが、やっぱり友達以上の恋人未満って事で相性とかもやっぱり大事なのでまずはホテルデートから始めたいなって考えています ( ˶'ᵕ'˶)

その時にゴムありのえっちでホテル別の2万円をお願いしたいなって思っています！

2回目以降にお会いする時は特にお金とか頂いたりするつもりは無いのでおうちデートとかLIVEとかも一緒に行けたら嬉しいです(⸝⸝ ´艸`⸝⸝)

その内容で良ければお返事貰えたら予定とか決めたいなって思っているのでお返事欲しいです！"""
func.send_conditional(user_name, user_address, mailaddress, password, text)