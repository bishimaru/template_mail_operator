import sqlite3

dbpath = 'firstdb.db'
conn = sqlite3.connect(dbpath)
# SQLiteを操作するためのカーソルを作成
cur = conn.cursor()

# データ検索
cur.execute('SELECT * FROM user')

# 取得したデータはカーソルの中に入る
for row in cur:
    print(row)

conn.close()