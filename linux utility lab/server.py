import socket
#Server
#decrypts columnar encrypted text
def decrypt(msg,key=[3,1,4,2]):
	l=len(key)
	l2=len(msg)/l
	orig_msg=['' for i in range(l)]
	curr = 1
	while curr<=l:
		for i in xrange(l):
			if key[i]==curr:
				temp=msg[:l2]
				msg=msg[l2:]
				orig_msg[i]=temp
				curr+=1
	#print orig_msg
	msg=''
	for i in xrange(l2):
		for j in xrange(l):	
			msg=msg+orig_msg[j][i]
	msg=msg.strip('*')
	#print msg
	return msg
 
host = ''        
port = 12345  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:
	data = conn.recv(1024)
	if not data:
		break
	print(data)
	print(decrypt(data))
conn.close()
