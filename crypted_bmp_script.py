MAXBYTE = 256
HEADERSIZE = 14
KEYLEN = 36

def rec(pos, cnt, bf_size, ind, cr_bytes, val):
	if pos == bf_size:
		if cnt == val:
			return cnt
	else:
		for byte in range(MAXBYTE):
			cnt += byte ^ cr_bytes[ind]
			rec(pos + 1, cnt, bf_size, ind + 1, cr_bytes, val)


def check_header(crypted_bytes):
	bf_type, bf_size = ['B', 'M'], 4
	byte_reserved1, byte_reserved2 = 0, 0
	pix_indent = 4
	size = len(crypted_bytes)
	key_bytes = []

	for i in range(len(bf_type)):
		for key_byte in range(MAXBYTE):
			if crypted_bytes[i] ^ key_byte == bf_type[i]:
				key_bytes.append(key_byte)
				break
	key_bytes += rec(0, 0, bf_size, 2, crypted_bytes, size)
	key_bytes += rec(0, 0, 2, 6, crypted_bytes, 0)
	key_bytes += rec(0, 0, 2, 8, crypted_bytes, 0)

	#понять где начинается картинка, т.е. чему равны следующие 4 байта ключа


with open('qr.enc.bmp', 'rb') as fin:
	s = fin.read()


check_header(s)
#check_info(s)