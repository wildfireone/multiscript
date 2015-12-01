import sqlite3

#connect to (and create if it does not exist) our database called testdata.db
conn = sqlite3.connect('testdata.db')
print "Opened database successfully"

#create a tables called CPU, with the columns TIME and CPUUSE - both of these values are stored simply as text 
conn.execute('''CREATE TABLE CPU (TIME TEXT, CPUUSE TEXT);''')
print "Table created successfully"

#remember to close the connection
conn.close()

