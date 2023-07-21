from widget import happymail

def fst_mail_hm():
  name_list = [
    "えりか", "くみ",
    "りな", "めあり",
    "きりこ", "彩香",
    "ハル", "ゆりあ",
    "みづき", "ももか",
    "りこ", "ゆうこ",
    "まいこ", "みすず"
  ]
  try:
    happymail.send_fst_message(name_list)
  except Exception as e:
    print(e)


if __name__ == '__main__':
  fst_mail_hm()
      