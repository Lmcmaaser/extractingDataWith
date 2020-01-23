import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter a URL to parse -') #prompt for a file
data = urllib.request.urlopen(url, context=ctx).read()
info = json.loads(data)
#print(info)
total = 0
#loop through comment tags and find the count values then sum the numbers
for item in info['comments']:
    total = total + item['count']
print('comment count sum', total)
