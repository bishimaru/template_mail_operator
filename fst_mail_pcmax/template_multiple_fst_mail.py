import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from fst_mail_pcmax import pcmax
import sqlite3
from concurrent.futures import ThreadPoolExecutor
import traceback


def main(maji_soushin, chara_name_list):
  # 〜〜〜〜〜〜検索設定〜〜〜〜〜〜
  # メール送信数（上限なしは0）
  limit_send_cnt = 0
  # 地域選択（3つまで選択可能）
  select_areas = [
    "東京都",
    # "千葉県",
    # "埼玉県",
    "神奈川県",
    # "静岡県",
    "新潟県",
    # "山梨県",
    # "長野県",
    # "茨城県",
    # "栃木県",
    # "群馬県",
  ]
  # 年齢選択（最小18歳、最高60以上）
  youngest_age = "19"
  oldest_age = "39"
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

  user_sort = [
    "ログイン順",
    # "登録順", 
    # "自己PR更新順"
  ]
  
  dbpath = 'firstdb.db'
  conn = sqlite3.connect(dbpath)
  # SQLiteを操作するためのカーソルを作成
  cur = conn.cursor()
  # 順番
  # データ検索
  for chara_name in chara_name_list:
    cur.execute('SELECT * FROM pcmax WHERE name = ?', (chara_name,))
    for row in cur:
        # print("キャラ情報")
        # print(row)
        chara_name_list[chara_name]["login_id"] = row[2]
        chara_name_list[chara_name]["login_pass"] = row[3]
        chara_name_list[chara_name]["fst_message"] = row[5]
        chara_name_list[chara_name]["fst_message_img"] = row[6]
        chara_name_list[chara_name]["second_message"] = row[9]
  # 〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜sqlite用コード「

  if 3 < len(select_areas):
    print("選択地域は3つまでです。")
    return
  names = list(chara_name_list.keys())
  print(f"キャラ数　{len(names)}")
  print(select_areas)
  
  if len(names) == 4:
    with ThreadPoolExecutor(max_workers=4) as executor:
      func1_future = executor.submit(pcmax.send_fst_mail, names[0], chara_name_list[names[0]]["login_id"], chara_name_list[names[0]]["login_pass"], chara_name_list[names[0]]["fst_message"], chara_name_list[names[0]]["fst_message_img"], chara_name_list[names[0]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt, user_sort)
      func2_future = executor.submit(pcmax.send_fst_mail, names[1], chara_name_list[names[1]]["login_id"], chara_name_list[names[1]]["login_pass"], chara_name_list[names[1]]["fst_message"], chara_name_list[names[1]]["fst_message_img"], chara_name_list[names[1]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt, user_sort) 
      func3_future = executor.submit(pcmax.send_fst_mail, names[2], chara_name_list[names[2]]["login_id"], chara_name_list[names[2]]["login_pass"], chara_name_list[names[2]]["fst_message"], chara_name_list[names[2]]["fst_message_img"], chara_name_list[names[2]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt, user_sort) 
      func4_future = executor.submit(pcmax.send_fst_mail, names[3], chara_name_list[names[3]]["login_id"], chara_name_list[names[3]]["login_pass"], chara_name_list[names[3]]["fst_message"], chara_name_list[names[3]]["fst_message_img"], chara_name_list[names[3]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt, user_sort)
    func1_future.result()
    func2_future.result()
    func3_future.result()
    func4_future.result()
  elif len(names) == 3:
    with ThreadPoolExecutor(max_workers=3) as executor:
      func1_future = executor.submit(pcmax.send_fst_mail, names[0], chara_name_list[names[0]]["login_id"], chara_name_list[names[0]]["login_pass"], chara_name_list[names[0]]["fst_message"], chara_name_list[names[0]]["fst_message_img"], chara_name_list[names[0]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt, user_sort)
      func2_future = executor.submit(pcmax.send_fst_mail, names[1], chara_name_list[names[1]]["login_id"], chara_name_list[names[1]]["login_pass"], chara_name_list[names[1]]["fst_message"], chara_name_list[names[1]]["fst_message_img"], chara_name_list[names[1]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt, user_sort)
      func3_future = executor.submit(pcmax.send_fst_mail, names[2], chara_name_list[names[2]]["login_id"], chara_name_list[names[2]]["login_pass"], chara_name_list[names[2]]["fst_message"], chara_name_list[names[2]]["fst_message_img"], chara_name_list[names[2]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt, user_sort)
    func1_future.result()
    func2_future.result()
    func3_future.result()
  elif len(names) == 2:
    with ThreadPoolExecutor(max_workers=2) as executor:
      func1_future = executor.submit(pcmax.send_fst_mail, names[0], chara_name_list[names[0]]["login_id"], chara_name_list[names[0]]["login_pass"], chara_name_list[names[0]]["fst_message"], chara_name_list[names[0]]["fst_message_img"], chara_name_list[names[0]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt, user_sort)
      func2_future = executor.submit(pcmax.send_fst_mail, names[1], chara_name_list[names[1]]["login_id"], chara_name_list[names[1]]["login_pass"], chara_name_list[names[1]]["fst_message"], chara_name_list[names[1]]["fst_message_img"], chara_name_list[names[1]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt, user_sort)
    func1_future.result()
    func2_future.result()
  elif len(names) == 1:
    with ThreadPoolExecutor(max_workers=1) as executor:
      func1_future = executor.submit(pcmax.send_fst_mail, names[0], chara_name_list[names[0]]["login_id"], chara_name_list[names[0]]["login_pass"], chara_name_list[names[0]]["fst_message"], chara_name_list[names[0]]["fst_message_img"], chara_name_list[names[0]]["second_message"], maji_soushin, select_areas, youngest_age, oldest_age, ng_words, limit_send_cnt, user_sort)
    func1_future.result()
  else:
    print("キャラ数を正しく取得できませんでした")

if __name__ == '__main__':
  maji_soushin = False

  # sqlite用コード〜〜〜〜〜〜〜〜〜〜〜〜〜〜
  if len(sys.argv) > 1:
    if sys.argv[1] == str(1):
      maji_soushin = True
    elif sys.argv[1] == str(0):
      maji_soushin = False
  if len(sys.argv) == 3:
    name1 = sys.argv[2]
    chara_name_list = {
      name1:{},
    }
  elif len(sys.argv) == 4:
    name1 = sys.argv[2]
    name2 = sys.argv[3]
    chara_name_list = {
      name1:{}, name2:{},  
    }
  elif len(sys.argv) == 5:
    name1 = sys.argv[2]
    name2 = sys.argv[3]
    name3 = sys.argv[4]
    chara_name_list = {
      name1:{}, name2:{}, name3:{},
    }
  elif len(sys.argv) == 6:
    name1 = sys.argv[2]
    name2 = sys.argv[3]
    name3 = sys.argv[4]
    name4 = sys.argv[5]
    chara_name_list = {
      name1:{}, name2:{}, name3:{}, name4:{}, 
    }
  
  main(maji_soushin, chara_name_list)
  