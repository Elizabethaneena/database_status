import MySQLdb as mysql
import time

db = mysql.connect(host='localhost', user='root',password='anee123', db="INFORMATION_SCHEMA")
cur = db.cursor()

cur.execute('SHOW STATUS')
res = cur.fetchall()
r = dict(res)
print(f"Threads_connected : {r['Threads_connected']}")
print(f"Threads_created : {r['Threads_created']}")
print(f"Threads_running : {r['Threads_running']}")
print(f"Uptime : {r['Uptime']}")
print(f"Queries : {r['Queries']}")
print(f"Max_used_connections : {r['Max_used_connections']}")

cur.close()
