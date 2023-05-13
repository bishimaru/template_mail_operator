import setting
import sys
sys.path.append(setting.yua_sumire_path)
import h_foot
import p_foot
import post
import time


def do_post_foot(h_cnt, p_cnt):
    start_time = time.time() 
    is_finished = post.repost_happymail_pcmax()
    while True:
      elapsed_time = time.time() - start_time  # 経過時間を計算する
      if elapsed_time >= 420 and is_finished:
        start_time = time.time() 
        h_foot.h_foot(h_cnt)
        break
      else:
        time.sleep(10)
    p_foot.p_foot(p_cnt)
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