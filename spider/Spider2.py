#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import requests
import urllib
import time
import image
import re

url = 'https://tieba.baidu.com/p/3697059303'
r=requests.get(url)
html=r.text
soup = BeautifulSoup(html)
imgs = soup.find_all('img',class_='BDE_Image')
img_folder="E:\\picture\\"
for img in imgs:
    url=img.get('src')
    urls=url.split("/")
    content=urllib.urlopen(url).read()
    path=img_folder+str(time.time())+"."+urls[-1]
    f=file(path,"wb")
    f.write(content)


