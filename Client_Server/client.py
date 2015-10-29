import socket
import sys

try:
	arguments = sys.argv
	print("[DEBUG] The arguments are: ", arguments)
	sid = arguments[1]

	if(len(arguments) == 2):
		ip = 'localhost'
		port = 58040

	elif(len(arguments) == 4):
		if(arguments[2] == "-n"):
			ip = arguments[3]
		if(arguments[2] == "-p"):
			port = arguments[3]
		else:
			print("Invalid arguments")
			quit()

	elif(len(arguments) == 6):
		if(arguments[2] == "-n"):
			ip = arguments[3]
		if(arguments[2] == "-p"):
			port = arguments[3]
		if(arguments[4] == "-n"):
			ip = arguments[5]
		if(arguments[4] == "-p"):
			port = int(arguments[5])
		else:
			print("Invalid arguments")
			quit()

	else:
		print("Invalid number of arguments")
		quit()

	print("[DEBUG] IP: ", ip, " | Port: ", port)


	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	command = input("Command: ")

	while(command != "exit"):

		if(command == "list"):
			word_sent = "TQR\n"

		elif(command[:7] == "request"):
			topic_number = command[8] #os espacos nao contam
			word_sent = "TER " + topic_number + "\n"

		elif(command[:6] == "submit"):
			#word_sent = "RQS " + sid + 
			pass

		clientSocket.sendto(word_sent.encode('utf-8'), (ip, port))
		data, addr = clientSocket.recvfrom(1024)
		data = data.decode()

		print("[DEBUG] Received command: ", data)

		if(data[:5] == "AWTES"):
			data = data.split()
			ip_tes = data[1]
			port_tes = int(data[2])
			clientSocket.close()
			tesSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			tesSocket.connect((ip_tes, port_tes))
			print ("[DEBUG] Connection estabilished to TES")
			word_sent = "RQT " + sid + "\n"
			tesSocket.sendall(word_sent.encode())
			fobj = open("received.pdf", "wb")
			l = tesSocket.recv(1024)
			while (l):
				print("[DEBUG] Downloading...")
				fobj.write(l)
				l = tesSocket.recv(1024)
			fobj.close()
			print("[DEBUG] File received")
			received_command = tesSocket.recv(1024)
			received_command = received_command.decode()
			print("lalalalal" , received_command)

		elif(data[:3] == "AWT"):
			data = data.split()
			for i in range(1, len(data) - 1): 
				print (str(i) + " - " + data[i + 1])

		command = input("\nCommand: ")

finally:
	tesSocket.close()