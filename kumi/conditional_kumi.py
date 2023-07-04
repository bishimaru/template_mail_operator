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
  user_name = str(sys.argv[1])
  user_address = str(sys.argv[2])

mailaddress = 'kumi414510@gmail.com'
password = 'afhbvdtdsvkvkvle'
text = """メアド交換ありがとうございます♪

お互いに出会えて良かったと感じる関係になることが理想です♪ただ、私はセフレの相性は1回では分からないと思いますので、最初に会う際にはホテル代とは別に2万円を預けてもらいたいです！

次回以降のデートのたびに、1万円ずつお返しする形で、最低でも3回はお会いできるようになります。その間にお互いの相性を確かめられれば、長期的なセフレとしての関係を築いていけると思っています(｀・ω・´)

メールいただく中でいろんな人とやり取りしてもしょうがないので、これでお返事くれる人とこれからの予定とか決めたいです♪

返信くれたら私からまたお話ししますね！よろしくお願いします！"""
func.send_conditional(user_name, user_address, mailaddress, password, text)