#import string
#from secret import MSG

#def encryption(msg):
#    ct = []
#    for char in msg:
#        ct.append((123 * char + 18) % 256)
#    return bytes(ct)

#ct = encryption(MSG)
#f = open('./msg.enc','w')
#f.write(ct.hex())
#f.close()


def decryption(msg):
	pt = []
	for char in msg:
		char = char - 18
		char = 179 * char % 256
		pt.append(char)
	return bytes(pt)

with open('msg.enc') as f:
	ct = bytes.fromhex(f.read())

pt = decryption(ct)
print(pt)
