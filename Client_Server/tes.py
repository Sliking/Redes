import socket
import sys
import time
import datetime
import os

try:
	arguments = sys.argv
	print("[DEBUG] The arguments are: ", arguments)

	if (len(arguments) == 1):
		port_tcp = 59000
		ecp_name = "localhost"
		port_udp = 59040

	else:
		print ("[ERROR] Invalid number of arguments")

	#Create TCP socket
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverSocket.bind(("localhost", port_tcp))
	serverSocket.listen(5)

	fobj = open("T01QF001.pdf", "rb")

	while 1:
		
			connection, client_adress = serverSocket.accept()
			print ("Connection from: ", client_adress)
			data = connection.recv(1024)
			data = data.decode()
			print(data)
			data = data.split()
			now = datetime.datetime.now()
			time = str(now.day) + now.strftime("%b") + str(now.year) + "_" + time.strftime("%X")
			deadline = str(now.day) + now.strftime("%b") + str(now.year) + "_00:00:00" 
			size = os.path.getsize("T01QF001.pdf")
			l = fobj.read(1024)
			while (l):
				print("[DEBUG] Sending...")
				connection.send(l)
				l = fobj.read(1024)
			fobj.close()
			word_sent = "AQT " + data[1] + "_" + time + " " + deadline + " " + str(size)
			connection.send(word_sent.encode())
			connection.close()

finally:
	serverSocket.close()