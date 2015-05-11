import urllib  
import urllib.request as request  
from bs4 import BeautifulSoup

def taobao(url):  
    response = request.urlopen(url)  
    html = response.read()  
    #我是win7系统，默认是gdk要先解码，再用utf8编码就可以显示汉字了  
    data = html.decode('gbk').encode('utf-8')  
    soup = BeautifulSoup(data)  
    for list in soup.find_all('h4'):  
        print(list.string)
        
if __name__ == '__main__':  
    print(""" 
+++++++++++++++++++++++ 
  学校：超神学院 
  专业：德玛班 
  姓名：德玛之力 
  version: python3.2 
+++++++++++++++++=++++ 
     """)  
    url = 'http://www.taobao.com/?spm=a310q.2219005.1581860521.1.b9kUd4'  
    taobao(url)  
