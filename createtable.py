import sqlite3

conn = sqlite3.connect('testdata.db')
print "Opened database successfully"

conn.execute('''CREATE TABLE CPU (TIME TEXT, CPUUSE TEXT);''')
print "Table created successfully"

conn.close()

