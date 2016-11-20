import socket, time, sys, random, threading

max_number_of_connections = 100500
max_time_for_waiting = 60

def gen_number():
	return str(random.randint(1000, 9999))

def check_symb(symb, ind):
	if (symb < b'0' or symb > b'9') and ind < 4:
		return False
	return True

def check_ind(i):
	return i == 4

def game(conn, addr):
	while True:
		num = list(gen_number())
		bulls, cows = 0, 0
		data = b""
		symb, ind = conn.recv(1), 0
		while symb:
			if not check_symb(symb, ind):
				print("error")
				sys.exit()
			if symb == b"\n":
				if not check_ind(ind):
					print(ind)
					print("error")
					sys.exit()
				print(bulls, cows)
				data = (str(bulls) + " " + str(cows)).encode("utf-8")
				conn.send(data)
				if bulls == 4:
					print("win")
					break
				bulls, cows = 0, 0
				symb, ind = conn.recv(1), 0
			else:
				if symb.decode("utf-8") == num[ind]:
					bulls += 1
				elif symb.decode("utf-8") in num:
					cows += 1
				symb, ind = conn.recv(1), ind + 1

def main(conn, addr):
	conn.settimeout(max_time_for_waiting)
	game(conn, addr)

if __name__ == "__main__":
	sock = socket.socket()
	PORT = int(sys.argv[1])
	sock.bind(("", PORT))
	sock.listen(max_number_of_connections)

	while True:
		t = threading.Thread(target=main, args=sock.accept())
		t.daemon = True
		t.start()











