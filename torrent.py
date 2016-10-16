import bencode, hashlib

with open('pincode_torrent.torrent', 'rb') as fin:
	torrent = bencode.bdecode(fin.read())
info = torrent['info']
piece_length = info['piece length']

for elem in info['files']:
	name, size = elem['path'][0], elem['length']
	if name == 'pincode':
		piece_length -= size
		continue
	if name == 'lena512color.tiff':
		with open(name, 'rb') as fin:
			chunk_id = size // piece_length
			fin.read(chunk_id * piece_length)
			lena_tiff = fin.read()
			piece_length -= len(lena_tiff)
	else:
		with open(name, 'rb') as fin:
			lena_mat = fin.read(piece_length)

hash = info['pieces'][chunk_id * 20:(chunk_id + 1) * 20]
i, h = -1, ''
while h != hash:
	i += 1
	h = hashlib.sha1(lena_tiff + str(i) + lena_mat).digest()
print(i)