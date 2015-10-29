import os

def get_nmap(options, ip):
	print("[DEBUG] Checking ports with nmap")
	command = "nmap " + options + " " + ip
	process = os.popen(command)
	result = str(process.read())
	print("[DEBUG] NMAP -> DONE!")
	return result