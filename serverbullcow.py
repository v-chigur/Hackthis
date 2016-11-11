import socket, time, sys, random

def gen_number():
	return str(random.randint(1000, 9999))

def game(conn, addr, num):
	bulls, cows = 0, 0
	data = b""
	symb, ind = conn.recv(1), 0
	while symb:
		if symb == b"\n":
			print(bulls, cows)
			data = (str(bulls) + " " + str(cows)).encode("utf-8")
			conn.send(data)
			if bulls == 4:
				print("win")
				main(conn, addr)
			bulls, cows = 0, 0
			symb, ind = conn.recv(1), 0
		else:
			if symb.decode("utf-8") == num[ind]:
				bulls += 1
			elif symb.decode("utf-8") in num:
				cows += 1
			symb, ind = conn.recv(1), ind + 1

def main(conn, addr):
	conn.settimeout(60)
	num = list(gen_number())
	game(conn, addr, num)

if __name__ == "__main__":
	sock = socket.socket()
	sock.bind(("", int(sys.argv[1])))
	sock.listen(100500)

	while True:
		main(*sock.accept())