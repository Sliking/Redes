import socket
import sys
import signal
import time


def server():

    arguments = sys.argv
    print ("[DEBUG] The arguments are: ", arguments)
    if(len(arguments) == 1):
        serverPort = 58040

    elif(len(arguments) == 3):
    	if(arguments[1] == "-p"):
    		serverPort = int(arguments[2])
    else:
    	print ("[ERROR] Invalid number of arguments", len(arguments))
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    print ("The server is ready to receive on port ", serverPort)
    while 1:
        data, addr = serverSocket.recvfrom(1024)
        command = data.decode()
        print ("Received command: ", command)

        if(command[:3] == "TQR"):
        	topic_list = []
        	topic_ip = []
        	topic_port = []
        	i = 0
        	fobj = open("topics.txt")
        	for line in fobj:
        		i += 1
        		topic = line.split()
        		topic_list.append(topic[0])
        		topic_ip.append(topic[1])
        		topic_port.append(topic[2])
        	word_sent = "AWT " + str(i)
        	for element in topic_list:
	        	word_sent += " " + element
        	word_sent += "\n"
        	fobj.close()

        elif(command[:3] == "TER"):
        	word_sent = "AWTES " + topic_ip[int(command[4]) - 1] + " " + topic_port[int(command[4]) - 1] + "\n"
        	print(word_sent)

        
        serverSocket.sendto(word_sent.encode('utf-8'), (addr[0], addr[1]))



def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if input("\nReally quit? (y/n)> ").lower().startswith('y'):
            sys.exit(1)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        sys.exit(1)

    # restore the exit gracefully handler here
    signal.signal(signal.SIGINT, exit_gracefully)


if __name__ == '__main__':
    # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    server()

