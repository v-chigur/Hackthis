import socket, time, sys, random, threading, json

def gen_number():
	return random.randint(1000, 9999)

def check_data(data, conn):
	error = 'Error: Sorry, the game requires a four-digit number. Try again to enter it.'
	info = json.dumps({'status': error, 'bulls': 0, 'cows': 0}).encode('utf-8')
	try:
		if data[-1] == b'\n':
			return True
		conn.send(info) 
		return False
	except:
			conn.send(info) 
			return False                                    

def game(conn, addr):
	conn.settimeout(60)
	while True:
		num = str(gen_number())
		bulls, cows = 0, 0
		data = conn.recv(5)
		if check_data(data):
			ind = 0
			symb = data[ind]
			state = 'continue'
			while symb:
				if bulls == 4:
					state = 'won'
				if ind == 3:
					info = json.dumps({'status': state, 'bulls': bulls, 'cows': cows}).encode('utf-8')
					conn.send(info)
					break
	
				if symb.decode("utf-8") == num[ind]:
					bulls += 1
				elif num.find(symb.decode("utf-8")) != -1:
					cows += 1
				symb, ind = data[ind + 1], ind + 1

def main(sock):
	while True:
		t = threading.Thread(target=game, args=sock.accept())
		t.daemon = True
		t.start()

if __name__ == "__main__":
	sock = socket.socket()
	try:
		port = int(sys.argv[1])
		sock.bind(("", port))
		sock.listen(100500)
	except:
		port = 8888

	sock.bind(("", port))
	sock.listen(100500)

	main(sock)