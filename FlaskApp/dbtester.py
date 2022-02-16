from dbmanager import DbManager

print('hello')
db = DbManager()
conn = db.conn

print(conn)
