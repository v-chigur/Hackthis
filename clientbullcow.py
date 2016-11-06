import socket, sys

conn = socket.socket()
conn.connect(("127.0.0.1", int(sys.argv[1])))

while True:
	bulls, cows = 0, 0
	alf, var = [], []
	for i in range(10):
		conn.send(('%01x' % i).encode("utf-8") * 4 + b"\n")
		bulls = int(conn.recv(9).decode("utf-8").split()[0])
		conn.recv(1)
		for j in range(bulls):
			alf.append(str(i))
	for i in range(1000, 9999):
		abcd = [int(s) for s in list(str(i))]
		if abcd[0] in [abcd[1], abcd[2], abcd[3]]:
			continue
		elif abcd[1] in [abcd[2], abcd[3]]:
			continue
		elif abcd[2] == abcd[3]:
			continue
		var.append(abcd)
	for v in vars:
		data = ''.join([alf[i] for i in v])
		conn.send(data.encode("utf-8") + b"\n")
		bc = conn.recv(9).decode("utf-8").split()
		bulls, cows = int(bc[0]), int(bc[1])

		if bulls == 4 or data == b"":
			print("win")
		else:
			print("don't give up")
conn.close()