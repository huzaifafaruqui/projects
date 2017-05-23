# client.py  
import socket
import columnar

host = socket.gethostname()        
port = 12345 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)

conn, addr = s.accept()

print('Connected by', addr)

while True:
  	msg = conn.recv(1024)
  	if not msg:
 	   break
	print 'Encrypted message received', msg
	
	print 'Enter Key'
	key = raw_input()

	msg = columnar.decrypt(msg, key)
	print 'The decrypted message received from the server is', msg    

conn.close()
s.close()

