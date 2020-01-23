import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter an XML URL to parse -') #prompt for xml file

#read the file and get the comment tag
data = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')

total = 0
#loop through comment tags and find the count values then sum the numbers
for item in lst:
    total = total + int(item.find('count').text)
print(total)
