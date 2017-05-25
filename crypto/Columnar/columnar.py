'''
	Columnar Transposition Cipher
	Source: http://www.geeksforgeeks.org/columnar-transposition-cipher/
	Author: Mohd Huzaifa Faruqui
	Date: 23 May, 2017
'''

def get_order(key):
	#code to convert key to order 'HACK' = [3,1,2,4]
	#thankyou Harsh and Bhatt
	out = [i+1 for j in key for i,v in enumerate(sorted(list(key))) if j==v]
	return out


def encrypt(msg, key='HACK'):

	n = len(key)
	#Replace spaces with '_'
	msg_ = msg.replace(' ', '_')

	#Make len(msg)%len(key) = 0
	while len(msg_)%n!=0:
		msg_ = msg_ + '_'

	#Split into characters
	chars = list(msg_)     # list('foo') = ['f','o','o']

	matrix = []
	
	#create matrix
	for i in xrange(0, len(chars), n): #step size = len(key); At every step form new row
		matrix.append(chars[i:i+n])     

	'''
		msg = Geeks for Geeks
		matrix = [['G', 'e', 'e', 'k'], ['s', '_', 'f', 'o'], ['r', '_', 'G', 'e'], ['e', 'k', 's', '_']]
	''' 
 	
	key_ = get_order(key)

	encrypt_msg = [None]*n #Empty list of size n

	for i in xrange(n):
		col = [row[i] for row in matrix]  #Pick ith element of each row i.e get ith column
		encrypt_msg[key_[i] - 1] = col  #Store ith column in position key[i] of encrypt_msg

	#encrypt_msg = [['e', '_', '_', 'k'], ['e', 'f', 'G', 's'], ['G', 's', 'r', 'e'], ['k', 'o', 'e', '_']]
		
	final_msg = ''.join([''.join(item) for item in encrypt_msg])

	# final_msg = e__kefGsGsrekoe_

	return final_msg

def decrypt(msg, key='HACK'):

	n = len(key)
	clen = len(msg)/n  #column length

	#Split into characters
	chars = list(msg)     # list('foo') = ['f','o','o']
	
	key_ = get_order(key)
	matrix = [[None]*n for i in xrange(clen)]
	
	for i in xrange(n):
		cno = key_[i] - 1 #Find key_[i]th column in text 
		col = chars[cno*clen:(cno+1)*clen]   # col 1 will be substr char[0:clen] ; col 2 will be substr[clen:2*clen]...
		
		for rno, item in enumerate(col):  #rno- row no for each letter
			matrix[rno][i] = item   

	# matrix = [['G', 'e', 'e', 'k'], ['s', '_', 'f', 'o'], ['r', '_', 'G', 'e'], ['e', 'k', 's', '_']]

	original_msg = ''.join([''.join(item) for item in matrix])
	
	return original_msg.replace('_', ' ')