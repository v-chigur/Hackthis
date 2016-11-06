import socket, sys

conn = socket.socket()
conn.connect(("127.0.0.1", int(sys.argv[1])))

while True:
	bulls, cows = 0, 0
	alf, var = [], []
	for i in range(10):
		conn.send(('%01x' % i).encode("utf-8") * 4 + b"\n")
		bulls = int(conn.recv(3).decode("utf-8").split()[0])
		for j in range(bulls):
			alf.append(str(i))
	abcd = [0, 0, 0, 0]
	for abcd[0] in range(4):
		for abcd[1] in range(4):
			if abcd[0] == abcd[1]:
				continue
			for abcd[2] in range(4):
				if abcd[2] in [abcd[0], abcd[1]]:
					continue
				for abcd[3] in range(4):
					if abcd[3] in [abcd[0], abcd[1], abcd[2]]:
						continue
					var.append(''.join([alf[i] for i in abcd]))
	for data in var:
		conn.send(data.encode("utf-8") + b"\n")
		bc = conn.recv(3).decode("utf-8").split()
		bulls, cows = int(bc[0]), int(bc[1])

		if bulls == 4 or data == b"":
			print("win", data)
			break
		else:
			print("don't give up")
conn.close()