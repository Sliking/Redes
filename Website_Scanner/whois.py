import os

def get_whois(url):
	print("[DEBUG] whois command")
	command = "whois " + url
	process = os.popen(command)
	result = str(process.read())
	print("[DEBUG] whois -> DONE!")
	return result