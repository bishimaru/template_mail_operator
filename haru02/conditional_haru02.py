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

mailaddress = 'k.haru414510@gmail.com'
password = 'vluwgzzzgjsudvsf'

text = """アドレスありがとうです！(._. )
PCMAXのはるです〜

実は私はこういうところで募集するのは初めてで..
目的が一緒の一人の長期さんを見つけたら辞めるつもりでいます！

なので本気で私と長期的な関係を続ける前提で会ってくれるか確かめたいので、最初に会う時はホテル代とは別に2万円は出してくれる方とお会いしたいと思っています(＞人＜;)
もし会いたいってもし思ってくれたら、お返事貰えたら凄く嬉しいです😳"""
func.send_conditional(user_name, user_address, mailaddress, password, text)