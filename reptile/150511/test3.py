import urllib.request as request  
import urllib.parse as parse  
import string  
import re  
import os  
import urllib.error as error  
print(""" 
+++++++++++++++++++++++ 
  学校：超神学院 
  专业：德玛班 
  姓名：德玛之力 
  version: python3.2 
+++++++++++++++++=++++ 
     """)  
def baidu_tieba(url, begin_page, end_page):  
    count = 1  
    for i in range(begin_page, end_page + 1):

        #生成保存位置，创建保存目录
        sName = 'C:/Users/xue82_000/Desktop/test/'+str(i).zfill(3)+'.jpg'     #生成保存位置
        print('正在下载第'+str(i)+'个页面, 并保存为'+sName)
        m = request.urlopen(url+str(i).zfill(3)+'.jpg').read()                #从链接中获取html全文内容

        with open(sName,'wb') as file:
            file.write(m)
        file.close()
        
if __name__ == "__main__":  
    url = "http://qiuld.com/qld/"  
    begin_page = 344
    end_page = 500
    baidu_tieba(url, begin_page, end_page)  
