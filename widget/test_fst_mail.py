import pcmax
import sys

# 〜〜〜〜〜〜キャラ情報〜〜〜〜〜〜
# name = ""
# login_id = ""
# login_pass = ""
# fst_message = """"""
# fst_message_img = ""

# 〜〜〜〜〜〜検索設定〜〜〜〜〜〜

# 地域選択（3つまで選択可能）
select_areas = [
  "東京都",
  "千葉県",
  # "埼玉県",
  "神奈川県",
]
# 年齢選択（最小18歳、最高60以上）
youngest_age = ""
oldest_age = "31"
# NGワード（複数、追加可能）
ng_words = [
  "通報",
  # "業者",
]


maji_soushin = False
if len(sys.argv) == 3:
  name = sys.argv[1]
  if sys.argv[2] == str(1):
    maji_soushin = True
  elif sys.argv[2] == str(0):
    maji_soushin = False

if 3 < len(select_areas):
  print("選択地域は3つまでです。")
else:
  pcmax.send_fst_mail(name, maji_soushin, select_areas, youngest_age, oldest_age, ng_words, )