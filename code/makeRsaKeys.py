import random, rabinMiller,cryptomath

def generateRSAkey(keySize=1024):
	p = rabinMiller.generateLargePrime(keySize)
	q = rabinMiller.generateLargePrime(keySize)
	n = p*q

	while True:
		e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
		if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
			break
	d = cryptomath.findModInverse(e, (p - 1) * (q - 1))

	publicKey = (n, e)
	privateKey = (n, d)


	return (publicKey,privateKey)

if __name__ == '__main__':
	publicKey,privateKey = generateRSAkey(1024)

	text = 'qwertyuiop'

	text = text.encode('ascii')
	text = list(text)
	en = []
	for e in text:
		en.append(pow(e,publicKey[1],publicKey[0]))

	print(en)

	de = []
	for c in en:
		de.append(pow(c, privateKey[1],privateKey[0]))
	
	text = bytes(de).decode('ascii')

	print(text)
	




	