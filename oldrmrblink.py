import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#定义nextpage函数
def next_page(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    dhtml=html.decode("gbk")
    soup = BeautifulSoup(dhtml, 'html.parser')
    tags = soup('a')
    nextpage= tags[11]
    url=nextpage.get('href', None)
    return url

#定义bs解析函数
def get_tag(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    dhtml=html.decode("gbk")
    soup = BeautifulSoup(dhtml, 'html.parser')
    tags = soup('a')
    return tags

#输入url并循环！！提取出nextpage url
url = next_page(input('Enter - '))
for i in range(1):
    url=next_page(url)
    print (url)
#得到url后又开始解析html得到tag
    tags=get_tag(url)
#对文内链接重复text代码
    for tag in [tags[11+2],tags[12+2],tags[13+2],tags[14+2],tags[15+2],tags[16+2],tags[17+2],tags[18+2],tags[19+2],tags[20+2],tags[21+2],tags[22+2],tags[23+2],tags[24+2],tags[25+2],tags[26+2],tags[27+2],tags[28+2],tags[29+2],tags[30+2]]:
        aurl=tag.get('href', None)
        print (aurl)
        ahtml = urllib.request.urlopen(aurl, context=ctx).read()
        adhtml=ahtml.decode("gbk")
        asoup = BeautifulSoup(adhtml, 'html.parser')
        asoup_title= asoup.find('div', class_ = 'div_biaoti')
        asoup_date= asoup.find('div', class_ = 'div_detail-cl')
        asoup_text= asoup.find('div', id = 'fontzoom')
        print (asoup_title.text)
        print (asoup_text.text)
        file = open(f"{asoup_title.text}.txt","w",encoding='utf-8')
        file.write(str(asoup_title.text + asoup_date.text + asoup_text.text))
        file.close()
