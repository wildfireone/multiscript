import sqlite3
import datetime
import time
import psutil


while True:
  #get current cpu percentage
  currentcpu = psutil.cpu_percent(interval=1)
  #get current time
  currenttime = datetime.datetime.now().time()

  #create the connection to the database
  conn = sqlite3.connect('testdata.db')
  print "Opened database successfully"

  #add the values into the database, use str() to turn the values into strings
  conn.execute("INSERT INTO CPU (TIME,CPUUSE) VALUES ('"+str(currenttime)+"','"+str(currentcpu)+"')")

  #commit the data to the databse
  conn.commit()
  print "Records created successfully";
  
  #close the connection
  conn.close()
  #wait ten seconds
  time.sleep(10)



