import urllib.request as request  
import urllib.parse as parse  
import string  
import re  
import os  
import urllib.error as error
from time import sleep
print(""" 
+++++++++++++++++++++++ 
  爬取邱璐东照片
  version: python3.2 
+++++++++++++++++=++++ 
     """)  
def baidu_tieba(url, begin_page, end_page):  
    count = 1  
    for i in range(begin_page, end_page + 1):


        #第一部分：爬页面
        #生成地址，获取内容，并打印提示
        m = request.urlopen(url+str(begin_page+1-count)).read()
        sName = 'C:/Users/xue82_000/Desktop/test1/'+str(i).zfill(3)+'.html'
        print('正在下载第'+str(i)+'个页面, 并保存为'+sName)

        #将网页内容写入sName，关闭
        with open(sName,'wb') as file:
            file.write(m)
        file.close()

        #第二部分：爬页面中的文件
        #文件夹部分
        #生成保存文件夹
        dirpath = 'C:/Users/xue82_000/Desktop/test1/'                          #生成目录地址
        dirname = str(i)
        new_path = os.path.join(dirpath, dirname)

        #若无此文件夹，则生成一个
        if not os.path.isdir(new_path):  
            os.makedirs(new_path)

        #读取源代码，并找出图片部分
        #读取一个网页源代码，解码
        page_data = m.decode('utf-8','ignore')                                #以utf-8解码，遇到未知参数ignore

        #生成图片匹配模版，并转化为模式对象，并遍历页面中所有图片
        page_image = re.compile('<img src=\"(.+?)\"')
        for image in page_image.findall(page_data):

            #生成图片匹配模版，并判断取出元素是否为url路径
            pattern = re.compile(r'^http://.*.jpg$')
            if  pattern.match(image):                                         #匹配，判断循环取出元素是否为图片格式
                try:

                    #找到图片，保存图片部分
                    #获取图片内容，生成图片名称，打印图片本地地址
                    image_data = request.urlopen(image).read()                #获取图片内容
                    image_path = dirpath + dirname +'/'+str(count)+'.jpg'     #生成图片地址
                    count += 1
                    print(image_path)

                    #打开图片文件，将图片内容写入文件，关闭图片文件
                    with open(image_path, 'wb') as image_file:
                        image_file.write(image_data)
                    image_file.close()
                except error.URLError as e:
                    print('Download failed')

        
if __name__ == "__main__":  
    url = "http://tieba.baidu.com/p/"  
    begin_page = 3756354889
    end_page = 3756354989
    baidu_tieba(url, begin_page, end_page)  
