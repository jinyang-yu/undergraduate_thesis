# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
html1=html.decode("gbk")
soup = BeautifulSoup(html1, 'html.parser')

# Retrieve all of the anchor tags
soup_title= soup.find('div', id = 'CenterH')
soup_text= soup.find('div', id = 'fontzoom')
print (soup_title.text)
print (soup_text.text)

file = open("1.txt","w")
file.write(str( soup_title.text + soup_text.text))
file.close()
