import sqlite3

dbpath = 'firstdb.db'
conn = sqlite3.connect(dbpath)
# SQLiteを操作するためのカーソルを作成
cur = conn.cursor()
mohu1 = "333"
mohu2 = "えりか"

# cur.execute('UPDATE happymail SET window_handle = ? WHERE name = ?', (mohu1, mohu2))

# データ検索
cur.execute('SELECT * FROM happymail')
# 取得したデータはカーソルの中に入る
for row in cur:
    print(row)
# データ検索
cur.execute('SELECT * FROM pcmax')
# 取得したデータはカーソルの中に入る
for row in cur:
    print(row)
# データ検索
cur.execute('SELECT * FROM gmail')
# 取得したデータはカーソルの中に入る
for row in cur:
    print(row)




conn.close()