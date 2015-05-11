import urllib.request as request  
import urllib.parse as parse  
import string  
print(""" 
+++++++++++++++++++++++ 
  学校：超神学院 
  专业：德玛班 
  姓名：德玛之力 
  version: python3.2 
+++++++++++++++++=++++ 
     """)  
def baidu_tieba(url, begin_page, end_page):  
    for i in range(begin_page, end_page + 1):  
        sName = 'C:/Users/xue82_000/Desktop/test/'+str(i).zfill(3)+'.html'     #生成保存位置
        print('正在下载第'+str(i)+'张图片, 并保存为'+sName)  
        m = request.urlopen(url+str(i).zfill(3)+'.jpg').read()                #生成url位置，并读取文件内容
        with open(sName,'wb') as file:  
            file.write(m)  
        file.close()  
if __name__ == "__main__":  
    url = "http://qiuld.com/qiuld/"  
    begin_page = 1  
    end_page = 10 
    baidu_tieba(url, begin_page, end_page)  
