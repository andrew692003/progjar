import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# Bind the socket to the port
server_address = ('localhost',9999)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

while True:
    	# Wait for a connection
    	# print >>sys.stderr, 'waiting for a connection'
    	connection, client_address = sock.accept()
    	# print >>sys.stderr, 'connection from', client_address
    	# Receive the data in small chunks and retransmit it
    	# while True:
        data = connection.recv(1024)
	#print data   
	file0 = data.split()
	file1 = file0[1]
	file2 = file1[1:]
	f = open(file2+".jpg",'r+')
	filedata = f.read()
	f.close()    	
	http_response = " HTTP/1.1 200 OK \n\n%s" %filedata
	
			# print >>sys.stderr, 'received "%s"' % data
            	# if data:
                #	print >>sys.stderr, 'sending data back to the client'
                #	connection.sendall(data)
            	# else:
                #	print >>sys.stderr, 'no more data from', client_address
                #	break
        # Clean up the connection
	connection.sendall(http_response)
	connection.close()
