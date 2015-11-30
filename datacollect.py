import sqlite3
import datetime
import time
import psutil


while True:
  #get current cpu percentage
  currentcpu = psutil.cpu_percent(interval=1)
  #get current time
  time = datetime.datetime.now().time()

  #create the connection to the database
  conn = sqlite3.connect('testdata.db')
  print "Opened database successfully"

  #add the values into the database
  conn.execute("INSERT INTO CPU (TIME,CPUUSE) VALUES ('"+time+"','"+currentcpu+"')")

  conn.commit()
  print "Records created successfully";
  conn.close()
  time.sleep(10)



