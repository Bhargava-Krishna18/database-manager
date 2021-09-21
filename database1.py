import MySQLdb as mysql
import time
import json
import pprint

db = mysql.connect(host='localhost', user='root', password='12345', db="INFORMATION_SCHEMA")
cur = db.cursor()
cur.execute('SHOW STATUS')
res = cur.fetchall()
r = dict(res)
pprint.pprint(r)

def database_info():
	print(f"Uptime, {r['Uptime']}")
	print(f"Queries, {r['Queries']}")
	print(f"Threads_connected, {r['Threads_connected']}")
	print(f"Threads_created, {r['Threads_created']}")
	print(f"Threads_running, {r['Threads_running']}")
	print(f"Max_used_connections, {r['Max_used_connections']}")

def process_list():
	cur.execute("select ID,DB from PROCESSLIST") 
	res = cur.fetchall()
	print(res)

def menu():
	print("1.Show Database Information")
	print("2.Show process list")
	print("3.Exit")

while True:
	menu()
	ch = input("Enter Choice: ")
	if ch == '1':
		database_info()
	elif ch == '2':
		process_list()
	elif ch == '3':
		break
	else:
		print("Invalid input")
