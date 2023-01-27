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
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
first= tags[17]
url1=first.get('href', None)
print (url1)

html1 = urllib.request.urlopen(url1, context=ctx).read()
soup1 = BeautifulSoup(html1, 'html.parser')
tags1 = soup1('a')
first1= tags1[17]
url2=first1.get('href', None)
print (url2)

html2 = urllib.request.urlopen(url2, context=ctx).read()
soup2 = BeautifulSoup(html2, 'html.parser')
tags2 = soup2('a')
first2= tags2[17]
url3=first2.get('href', None)
print (url3)

html3 = urllib.request.urlopen(url3, context=ctx).read()
soup3 = BeautifulSoup(html3, 'html.parser')
tags3 = soup3('a')
first3= tags3[17]
url4=first3.get('href', None)
print (url4)

html4 = urllib.request.urlopen(url4, context=ctx).read()
soup4 = BeautifulSoup(html4, 'html.parser')
tags4 = soup4('a')
first4= tags4[17]
url5=first4.get('href', None)
print (url5)

html5 = urllib.request.urlopen(url5, context=ctx).read()
soup5 = BeautifulSoup(html5, 'html.parser')
tags5 = soup5('a')
first5= tags5[17]
url6=first5.get('href', None)
print (url6)

html6 = urllib.request.urlopen(url6, context=ctx).read()
soup6 = BeautifulSoup(html6, 'html.parser')
tags6 = soup6('a')
first6= tags6[17]
url7=first6.get('href', None)
print (url7)
