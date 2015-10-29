import os

def create_dir(directory):
	print("[DEBUG] Checking folder")
	if not os.path.exists(directory):
		os.makedirs(directory)
		print("[DEBUG] Created folder -> DONE!")

def write_file(path, data):
	print("[DEBUG] Writing in file")
	f = open(path, 'w')
	f.write(data)
	f.close()
	print("[DEBUG] Write -> DONE!")