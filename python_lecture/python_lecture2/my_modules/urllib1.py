from urllib import request 
url = "https://www.google.com"
html = request.urlopen(url).read()

import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = request.urlopen(url, context=ctx).read()