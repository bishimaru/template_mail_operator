import time

def timer(fnc, seconds, h_cnt, p_cnt):  
  start_time = time.time() 
  is_finished = fnc(h_cnt, p_cnt)
  while True:
    elapsed_time = time.time() - start_time  # 経過時間を計算する
    if elapsed_time >= seconds and is_finished:
      start_time = time.time() 
      break
    else:
      time.sleep(10)
  return True