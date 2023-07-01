import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import setting
import check_mail
sys.path.append(setting.misuzu_path)
import repost_misuzu
import h_foot_misuzu
# import p_foot_misuzu
import time

def do_post_foot(h_cnt, p_cnt):
    start_time = time.time() 
    repost_misuzu.repost_happymail_pcmax()
    # check_mail.check_mail()

    while True:
      elapsed_time = time.time() - start_time  # 経過時間を計算する
      if elapsed_time >= 300:
        start_time = time.time() 
        h_foot_misuzu.h_foot(h_cnt)
        # p_foot_misuzu.p_foot(p_cnt)
        break
      else:
        time.sleep(10) 
    return True
if __name__ == '__main__':
  if len(sys.argv) < 2:
    h_cnt = 20
    p_cnt = 10
  elif len(sys.argv) == 2:
    h_cnt = int(sys.argv[1])
    p_cnt = 10
  else:
    h_cnt = int(sys.argv[1])
    p_cnt = int(sys.argv[2])
  do_post_foot(h_cnt, p_cnt)