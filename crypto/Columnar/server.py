import socket                                         
import columnar

host = socket.gethostname()    
port = 12345                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
 
print 'Enter message'
msg = raw_input()

print 'Enter Key'
key = raw_input()

encrypt_msg = columnar.encrypt(msg, key)
 
s.sendall(encrypt_msg)

s.close()                     
