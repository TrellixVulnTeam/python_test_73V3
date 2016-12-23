import sqlite3
import csv

with open('members.csv', newline='') as f:
  csv_reader = csv.DictReader(f)
  members = [
  	(row['名字'], row['團體'])
  	for row in csv_reader
  ]

with open('create_db.sql') as f:
	create_db_sql = f.read()

db = sqlite3.connect('members.db')
with db:
	db.executescript(create_db_sql)


with db:
	db.executemany(
			'insert into members(name, group_name) values(?,?)',
			members
		)