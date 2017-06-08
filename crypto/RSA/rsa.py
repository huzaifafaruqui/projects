import random




def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a


def gen_key(p, q):
	n = p*q

	phi = (p-1)*(q-1)

	e = 2

	while gcd(e, phi)!=1:   #find coprime to phi
		e += 1

	for i in xrange(1, phi):  #find multiplicative inverse to e  = d
		if (i*e)%phi == 1:
			d = i 

	#public key - (e,n)

	#private - key(d, n)

	return ((e,n), (d,n))		

def encrypt(msg, key):
	e, n = key

	return pow(msg, e, n)		 


def decrypt(msg, key):
	d, n = key

	return pow(msg, d, n)


p = int(raw_input())
q = int(raw_input())
msg = int(raw_input())  #less than p*q

puk, pvk = gen_key(p, q)

enc = encrypt(msg, puk)

print decrypt(enc, pvk)
