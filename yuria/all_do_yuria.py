import setting
import sys
sys.path.append(setting.yuria_path)
import h_foot_yuria
import p_foot_yuria
import post_yuria
import time

def do_post_foot():
    if len(sys.argv) < 2:
      cnt = 20
    else:
      cnt = int(sys.argv[1])
    start_time = time.time() 
    is_finished = post_yuria.repost_happymail_pcmax()
    while True:
      elapsed_time = time.time() - start_time  # 経過時間を計算する
      if elapsed_time >= 300 and is_finished:
        start_time = time.time() 
        h_foot_yuria.h_foot(cnt)
        break
      else:
        time.sleep(10)
    # p_foot_yuria.p_foot(cnt)
    return True

if __name__ == '__main__':
  print(f'__name__ は{__name__}となっている。')
  do_post_foot()