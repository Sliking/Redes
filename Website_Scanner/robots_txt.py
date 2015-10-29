import urllib.request
import io

def get_robots_txt(url):
	print("[DEBUG] Getting robots.txt")
	if url.endswitch('/'):
		path = url
	else:
		path = url + '/'
	req = urllib.request.urlopen(path + "robots.txt", data = None)
	data = io.TextIOWrapper(req, encoding = 'utf-8')
	print("[DEBUG] Robots.txt -> DONE!")
	return data.read()