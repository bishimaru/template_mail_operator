import time

def timer(fnc, seconds, h_cnt, p_cnt):  
  start_time = time.time() 
  fnc(h_cnt, p_cnt)
  while True:
    elapsed_time = time.time() - start_time  # 経過時間を計算する
    if elapsed_time >= seconds:
      start_time = time.time() 
      break
    else:
      time.sleep(10)
  return True

def send_gmail():
  print(246)