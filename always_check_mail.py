from check_mail import check_mail
import time

def timer(sec, functions):
  start_time = time.time() 
  for func in functions:
    func()
  elapsed_time = time.time() - start_time  # 経過時間を計算する
  while elapsed_time < sec:
    time.sleep(10)
    elapsed_time = time.time() - start_time  # 経過時間を計算する
    print(elapsed_time)
while True:
  timer(480, [check_mail])