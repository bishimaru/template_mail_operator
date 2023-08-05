import pcmax
import sys
import sqlite3
# 〜〜〜〜〜〜キャラ情報〜〜〜〜〜〜
# name = "ゆりあ"
# login_id = "18983588"
# login_pass = "6667"
# fst_message = """初めまして！ゆりあって言います♪
# 都内で不動産関係のOLをしています！

# 仕事に少し慣れてきたこともあり、仕事終わりにお家に帰ると人肌恋しさを感じるようになってきました(>_<)
# いっぱいいちゃいちゃできるようなせふれさんとここで出会えたらいいなって思ってます( ´ ▽ ` )

# 同じように人肌恋しいって感じたことありませんか？？"""
# fst_message_img = ""

# 〜〜〜〜〜〜検索設定〜〜〜〜〜〜

# 地域選択（3つまで選択可能）
select_areas = [
  "東京都",
  # "千葉県",
  "埼玉県",
  "神奈川県",
]
# 年齢選択（最小18歳、最高60以上）
youngest_age = ""
oldest_age = "35"
# NGワード（複数、追加可能）
ng_words = [
  "通報",
  "業者",
  "食事",
  "お茶",
  "円",
  "パパ",
  "援",
  "援交",
  "お金のやり取り",
]


maji_soushin = False
# if len(sys.argv) == 2:
#   if sys.argv[1] == str(1):
#     maji_soushin = True
#   elif sys.argv[1] == str(0):
#     maji_soushin = False
# elif len(sys.argv) >= 3:
#   print("引数を正しく入力してください")

# sqlite用コード〜〜〜〜〜〜〜〜〜〜〜〜〜〜
if len(sys.argv) == 3:
  name = sys.argv[2]
  if sys.argv[1] == str(1):
    maji_soushin = True
  elif sys.argv[1] == str(0):
    maji_soushin = False
elif len(sys.argv) > 3:
  print("引数を正しく入力してください")

dbpath = 'firstdb.db'
conn = sqlite3.connect(dbpath)
# SQLiteを操作するためのカーソルを作成
cur = conn.cursor()
# 順番
# データ検索
cur.execute('SELECT * FROM pcmax WHERE name = ?', (name,))
for row in cur:
    print("キャラ情報")
    print(row)
    login_id = row[2]
    login_pass = row[3]
    fst_message = row[5]
    # print(row)
    fst_message_img = row[6]
# 〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜sqlite用コード「




# if 3 < len(select_areas):
#   print("選択地域は3つまでです。")
# else:
#   pcmax.send_fst_mail(name, login_id, login_pass, fst_message, fst_message_img, maji_soushin, select_areas, youngest_age, oldest_age, ng_words, )
if 3 < len(select_areas):
  print("選択地域は3つまでです。")
else:
  pcmax.send_fst_mail(name, login_id, login_pass, fst_message, fst_message_img, maji_soushin, select_areas, youngest_age, oldest_age, ng_words, )