MAXBYTE = 256
HEADERSIZE = 14
KEYLEN = 36

with open('qr.enc.bmp', 'rb') as fin:
	crypted_bytes = fin.read()

bf_type, bf_size = ['B', 'M'], 4
fin_size = len(crypted_bytes)
bf_res = 0
original_header = ''.join(bf_type).encode() + fin_size.to_bytes(bf_size, byteorder='big')
original_header += 2 * bf_res.to_bytes(2, byteorder='big')