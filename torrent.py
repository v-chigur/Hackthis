import bencode, os

with open('pincode_torrent.torrent', 'rb') as fin:
	torrent = bencode.bdecode(fin.read())
	info = torrent['info']
	piece_length = info['piece length']
	piece, pieces = '', []
	for file_info in info['files']:
		path = os.sep.join([info['name']] + file_info['path'])
		sfile = open(path.decode('UTF-8'), "rb")
		pieces.append(sfile.read(piece_length))
		sfile.close()
	print(*pieces)