from math import sqrt
from itertools import cycle

MAXBYTE = 256
HEADERSIZE = 14
KEYLEN = 36

with open('qr.enc.bmp', 'rb') as fin:
	crypted_bytes = fin.read()

bf_type, bf_size = ['B', 'M'], 4
fin_size = len(crypted_bytes)
bf_res, c_planes, bits = 0, 1, 24
bh_size, bi_size = 14, 40
indent = bh_size + bi_size
compression = 0
original_bytes= ''.join(bf_type).encode() + fin_size.to_bytes(bf_size, byteorder='little')
original_bytes += 2 * bf_res.to_bytes(2, byteorder='little') + (indent).to_bytes(4, byteorder='little')
original_bytes += (bi_size).to_bytes(4, byteorder='little')

x, mx = 4, 4
while (mx * mx <= fin_size - indent):
	if mx % 4 == 0:
		x = mx
	mx += 1

original_bytes += 2 * (x).to_bytes(4, byteorder='little') + (c_planes).to_bytes(2, byteorder='little')
original_bytes += (bits).to_bytes(2, byteorder='little')
original_bytes += (compression).to_bytes(4, byteorder='little') + (x * x).to_bytes(4, byteorder='little')

key = [x ^ y for (x, y) in zip(original_bytes[:KEYLEN], crypted_bytes[:KEYLEN])]
original_bytes = [(x ^ y).to_bytes(1, byteorder='little') for (x, y) in zip(crypted_bytes, cycle(key))]

with open('qr.enc.bmp', 'wb') as fout:
	for b in original_bytes:
		fout.write(b)