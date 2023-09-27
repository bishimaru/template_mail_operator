import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from widget import func
import traceback
from email.mime.text import MIMEText
from email.utils import formatdate
import sqlite3


mailaddress = 'k.yuria.0722@gmail.com'
password = 'mbvjzdrerdljzbls'
text = """メアド交換ありがとうございます(^ ^)
ゆりあです♪

お互いに都合が良いときに人肌を埋めれるような関係が理想です！

あと最初会う時はホテルデートから始めたいんですけど、1回きりの出会いっていうのが私としては絶対嫌なのでホテル代と別に2万円を預けてもらいたいですm(_ _)m
2回目から5千円づつ返していけば最低でも4回は会えるし、その頃にはお互いのことを理解できてると思います♪

それでも大丈夫ならお返事もらえませんか？？"""
# func.send_conditional(user_name, user_address, mailaddress, password, text)

def conditional_mail(name, user_address):
  dbpath = 'firstdb.db'
  conn = sqlite3.connect(dbpath)
  # # SQLiteを操作するためのカーソルを作成
  cur = conn.cursor()
  # # 順番
  # # データ検索
  cur.execute('SELECT conditions_message, gmail_password FROM pcmax WHERE name = ?', (name,))
  for row in cur:
      text = row[0]
      password = row[1]
  cur.execute('SELECT gmail_password FROM gmail WHERE name = ?', (name,))
  for row in cur:
      mailaddress = row[0]
  func.send_conditional(name, user_address, mailaddress, password, text)
  
  

                 
  

if __name__ == '__main__':
  
  if len(sys.argv) == 3:
    name = str(sys.argv[1])
    user_address = str(sys.argv[2])
  else:
    print("引数を正しく入力してください")
    
  conditional_mail(name)
