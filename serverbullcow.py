import socket, time, sys, random

sock = socket.socket()
sock.bind(("", int(sys.argv[1])))
sock.listen(1)
conn, addr = sock.accept()
conn.settimeout(60)

num = list(str(random.randint(1000, 9999)))
#print("imagined num: " + ''.join(num))
bulls, cows = 0, 0
data = b""
symb, i = conn.recv(1), 0
while symb:
	if symb == b"\n":
		print(bulls, cows)
		data = (str(bulls) + " " + str(cows)).encode("utf-8")
		conn.send(data)
		bulls, cows = 0, 0
		symb, i = conn.recv(1), 0
	else:
		if symb.decode("utf-8") == num[i]:
			bulls += 1
		elif symb.decode("utf-8") in num:
			cows += 1
		symb, i = conn.recv(1), i + 1
conn.close()