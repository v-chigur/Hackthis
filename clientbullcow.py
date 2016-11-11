import socket, sys, itertools

def get_vars(conn):
	bulls, cows = 0, 0
	alf = []
	for i in range(10):
		conn.send(('%01x' % i).encode("utf-8") * 4 + b"\n")
		bulls = int(conn.recv(3).decode("utf-8").split()[0])
		for j in range(bulls):
			alf.append(str(i))
	return itertools.permutations(tuple(alf))

def play(conn):
	for abcd in get_vars(conn):
		data = ''.join(abcd)
		conn.send(data.encode("utf-8") + b"\n")
		bc = conn.recv(3).decode("utf-8").split()
		bulls, cows = int(bc[0]), int(bc[1])

		if bulls == 4:
			print("win", data)
			main(conn)

def main(conn):
	play(conn)

if __name__ == "__main__":
	conn = socket.socket()
	conn.connect(("127.0.0.1", int(sys.argv[1])))

	while True:
		main(conn)