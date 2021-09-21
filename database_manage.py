import MySQLdb as mysql
import time
import json



from rich.prompt import Prompt
from rich import style
from rich.console import Console

console = Console()

db = mysql.connect(host='localhost', user='root', password='1234', db="INFORMATION_SCHEMA") #making connection
cur = db.cursor() #To allow to write queries
cur.execute('SHOW STATUS') #query
res = cur.fetchall() #Fetch all
r = dict(res)
print(r)

def database_info():
	print(f"Uptime, {r['Uptime']}" ,style = 'bold blue')
	print(f"Queries, {r['Queries']}" ,style = 'bold blue')
	print(f"Threads_connected, {r['Threads_connected']}" ,style = 'bold blue')
	print(f"Threads_created, {r['Threads_created']}" ,style = 'bold blue')
	print(f"Threads_running, {r['Threads_running']}" ,style = 'bold blue')
	print(f"Max_used_connections, {r['Max_used_connections']}" ,style = 'bold blue')

def process_list():
	cur.execute("select ID,DB from PROCESSLIST") 
	res = cur.fetchall()
	print(res)

def menu():
	print("1.Show Database Information" ,style = 'bold blue')
	print("2.Show process list" ,style = 'bold red')
	print("3.Exit" ,style = 'bold #7C53E7')

while True:
	menu()
	ch = int(input("Enter Choice: "))
	if ch == 1:
		database_info()
	elif ch == 2:
		process_list()
	elif ch == 3:
		break
	else:
		print("Invalid input")
