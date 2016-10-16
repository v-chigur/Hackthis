import bencode, hashlib, struct

MAXBYTE = 256
bencode_size = 4
hsh_length = 40
num_pieces = 24

def get_hash(file_name, piece_length, x):
	with open(file_name, 'rb') as fin:
		s = fin.read()
		if x > 0:
			chuncks = [s[:x]] + [s[i:i+piece_length] for i in range(x, len(s), piece_length)]
		else:
			chuncks = [s[i:i+piece_length] for i in range(x, len(s), piece_length)]
		hash = ''
		for chunk in chuncks:
			hash += hashlib.sha1(chunk).hexdigest()
	return (chuncks, hash)

with open('pincode_torrent.torrent', 'rb') as fin:
	torrent = bencode.bdecode(fin.read())
info = torrent['info']
piece_length = info['piece length']
pieces = [info['pieces'][i:i+piece_length] for i in range(0, len(info['pieces']), piece_length)]
hash_pieces = ''.join('%02x' % ord(x) for x in info['pieces'])

lena_tiff, lena_tiff_hsh = get_hash('lena512color.tiff', piece_length, 0)
x = len(lena_tiff[-1])
dlt_tiff =  piece_length - x
dlt_mat = dlt_tiff - bencode_size

lena_mat, lena_mat_hsh = get_hash('lena512.mat', piece_length, dlt_mat)
head = num_pieces * hsh_length
#print hash_pieces[:head] == lena_tiff_hsh[:head]
#print hash_pieces[head+hsh_length:] == lena_mat_hsh[hsh_length:]
torr_hsh = hash_pieces[head:head+hsh_length]
chunk = [lena_tiff[-1], '', lena_mat[0]]

for i in range(10000):
	chunk[1] = str(i)
	h = hashlib.sha1(''.join(chunk)).hexdigest()

	if (torr_hsh == h):
		print i
