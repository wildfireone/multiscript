import socket
import HTML
import sqlite3


#setup server
HOST, PORT = '', 8888
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
#run forever
while True:
    
    #standard server code
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    http_status = "HTTP/1.1 200 OK \n"
    http_type = "Content-Type: text/html\n"
    
    #create a new table with a title row
    cputable = HTML.Table(header_row=['TIME', 'CPUUSE'])
    
    #open database
    conn = sqlite3.connect('testdata.db')
    #get data from database
    cursor = conn.execute("SELECT TIME, CPUUSE FROM CPU")
    #for every row in our database
    for row in cursor:
      #add a new row to our table
      cputable.rows.append([row[0], row[1]])
    
    #close the connection
    conn.close()
    
    #now generate the HTML output
    #the meta tag here forces a page refresh content = 10 means this happens every 10 seconds
    http_body = """
	  <!doctype html>
	  <html>
	  <head>
	  	<title> my server data </title>
	  	<meta http-equiv="refresh" content="10" >
	  </head>
	  <body> 
	    """ + str(cputable) + """
	  </body>
	  </html>"""

    #finally send everything
    client_connection.send(http_status)
    client_connection.send(http_type)
    client_connection.send(http_body)
    client_connection.close()

