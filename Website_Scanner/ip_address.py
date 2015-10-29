import os

def get_ip_address(url):
	print("[DEBUG] Getting IP address")
	command = "host " + url
	process = os.popen(command)
	result = str(process.read())
	marker = result.find('has address') + 12
	print("[DEBUG] IP address -> DONE!")
	return result[marker:].splitlines()[0]