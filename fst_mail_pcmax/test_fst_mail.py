import pcmax
import sys

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
  # "埼玉県",
  "神奈川県",
]
# 年齢選択（最小18歳、最高60以上）
youngest_age = ""
oldest_age = ""
# NGワード（複数、追加可能）
ng_words = [
  "通報",
  # "業者",
]


maji_soushin = False
# if len(sys.argv) == 2:
#   if sys.argv[1] == str(1):
#     maji_soushin = True
#   elif sys.argv[1] == str(0):
#     maji_soushin = False
# elif len(sys.argv) >= 3:
#   print("引数を正しく入力してください")

if len(sys.argv) == 3:
  name = sys.argv[2]
  if sys.argv[1] == str(1):
    maji_soushin = True
  elif sys.argv[1] == str(0):
    maji_soushin = False
elif len(sys.argv) > 3:
  print("引数を正しく入力してください")




if 3 < len(select_areas):
  print("選択地域は3つまでです。")
else:
  pcmax.send_fst_mail(name, login_id, login_pass, fst_message, fst_message_img, maji_soushin, select_areas, youngest_age, oldest_age, ng_words, )