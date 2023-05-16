import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import setting
sys.path.append(setting.meari_path)
import h_foot_meari
import p_foot_meari
import post_meari
import time

def do_post_foot(h_cnt, p_cnt):
    start_time = time.time() 
    is_finished = post_meari.repost_happymail_pcmax()
    while True:
      elapsed_time = time.time() - start_time  # 経過時間を計算する
      if elapsed_time >= 360 and is_finished:
        start_time = time.time() 
        h_foot_meari.h_foot(h_cnt)
        break
      else:
        time.sleep(10)
    # p_foot_meari.p_foot(p_cnt)
    return True

if __name__ == '__main__':
  if len(sys.argv) < 2:
    h_cnt = 20
    p_cnt = 20
  elif len(sys.argv) == 2:
    h_cnt = int(sys.argv[1])
    p_cnt = 20
  else:
    h_cnt = int(sys.argv[1])
    p_cnt = int(sys.argv[2])
  do_post_foot(h_cnt, p_cnt)