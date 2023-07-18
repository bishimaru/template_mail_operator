from widget import happymail

def fst_mail_hm():
  name_list = [
    "えりか", "くみ",
    "りな", "めあり",
    "きりこ", "彩香",
    "ハル", "ゆりあ",
    "みづき", "ももか",
    "りこ", "ゆうこ"
  ]
  happymail.send_fst_message(name_list)


if __name__ == '__main__':
  fst_mail_hm()
      