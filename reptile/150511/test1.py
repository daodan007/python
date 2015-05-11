#coding=utf-8
import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImage(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = imgre.findall(html.decode('utf-8'))
    return imglist



html = getHtml("http://qiuld.com")

for each in getImage(html):
    print(each)
#    print('\r')

# print (getImage(html))
