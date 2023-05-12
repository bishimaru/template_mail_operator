import time

def timer(fnc, seconds):  
  start_time = time.time() 
  is_finished = fnc()
  while True:
    elapsed_time = time.time() - start_time  # 経過時間を計算する
    if elapsed_time >= seconds and is_finished:
      start_time = time.time() 
      break
    else:
      time.sleep(10)
  return True