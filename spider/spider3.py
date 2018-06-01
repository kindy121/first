#-*-coding:utf-8-*-

import threading
import traceback
from bs4 import BeautifulSoup
from proxy import KDLProxyFinder, ProxyPool

import requests

baseurl="http://www.plantphoto.cn/class"
r=requests.get(baseurl)
html=r.text
# soup = BeautifulSoup(html,"html.parser")
finder=KDLProxyFinder("http://www.kuaidaili.com/free/inha/")

ppool_instance=ProxyPool(finder)
ppool_instance.get_proxies()
r=requests.get(baseurl,proxies=ppool_instance.get_one_proxy())
html=r.text
print html
requests.request()