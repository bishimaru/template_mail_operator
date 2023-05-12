import setting
import sys
sys.path.append(setting.yua_sumire_path)
import h_foot
import p_foot
import post
import time


def do_post_foot():
    if len(sys.argv) < 2:
      cnt = 20
    else:
      cnt = int(sys.argv[1])    
    start_time = time.time() 
    is_finished = post.repost_happymail_pcmax()
    while True:
      elapsed_time = time.time() - start_time  # 経過時間を計算する
      if elapsed_time >= 420 and is_finished:
        start_time = time.time() 
        h_foot.h_foot(cnt)
        break
      else:
        time.sleep(10)
    p_foot.p_foot(cnt)
    return True

if __name__ == '__main__':
  do_post_foot()