import socket

#client side
#ecnrypts msg using columnar transposition

def encrypt(msg,key=[3,1,4,2]):
	l=len(key)
	encrypted_msg=['' for i in range(l)]
	
	while len(msg)%l!=0:
		msg=msg+'*'
	for i in xrange(l):
		temp=''
		for j in xrange(i,len(msg),l):
		#	print j
			temp+=msg[j]
		encrypted_msg[key[i]-1]=temp
 
 
	print encrypted_msg
	return ''.join(encrypted_msg)

host = socket.gethostname()    
port = 12345                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
msg=raw_input()
msg=encrypt(msg)
s.sendall(msg)
#data = s.recv(1024)
s.close()
