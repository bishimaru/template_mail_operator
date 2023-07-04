import time
import sqlite3

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

def get_windowhandle(site, name):
  # DB
  dbpath = 'firstdb.db'
  conn = sqlite3.connect(dbpath)
  # SQLiteを操作するためのカーソルを作成
  cur = conn.cursor()
  # データ検索
  # cur.execute('UPDATE happymail SET window_handle = ? WHERE name = ?', (mohu1, mohu2))
  if site == "happymail":
    cur.execute('SELECT window_handle FROM happymail WHERE name = ?', (name,))
  elif site == "pcmax":
    cur.execute('SELECT window_handle FROM pcmax WHERE name = ?', (name,))
  w_h = ""
  for row in cur:
    w_h = row[0]
  conn.close()

  return w_h