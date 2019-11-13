import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
url="https://www.ntu.edu.tw/"
with req.urlopen(url) as response:
	data=response.read().decode("utf-8")
print(data)

