import setting
import sys
sys.path.append(setting.meari_path)
import h_foot_meari
import p_foot_meari
import post_meari
import time

def do_post_foot():
    if len(sys.argv) < 2:
      cnt = 20
    else:
      cnt = int(sys.argv[1])
    start_time = time.time() 
    is_finished = post_meari.repost_happymail_pcmax()
    while True:
      elapsed_time = time.time() - start_time  # 経過時間を計算する
      if elapsed_time >= 360 and is_finished:
        start_time = time.time() 
        h_foot_meari.h_foot(cnt)
        break
      else:
        time.sleep(10)
    # p_foot_meari.p_foot(cnt)
    return True


if __name__ == '__main__':
  do_post_foot()