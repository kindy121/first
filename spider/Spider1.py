import requests
from bs4 import BeautifulSoup
import json

url="https://www.baidu.com/"
r=requests.get(url)
print(r.status_code)
print r.text

re=requests.get('http://202.114.144.21', params={'wd': 'python'})
print re.text
print "#######"


r = requests.post('https://api.github.com/some/endpoint', data=json.dumps({'some': 'data'}))
print(r.json())

import requests
import json

data = {'some': 'data'}
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

r = requests.post('https://api.github.com/some/endpoint', data=data, headers=headers)
print(r.text)

r = requests.get('http://www.itwhy.org')
print(r.text, '\n{}\n'.format('*'*79), r.encoding)
r.encoding = 'GBK'
print(r.text, '\n{}\n'.format('*'*79), r.encoding)

url='http://ip.taobao.com/service/getIpInfo.php'
try:
    r=requests.get(url,params={'ip':'8.8.8.8'},timeout=1)
    r.raise_for_status()
except requests.RequestException as e:
    print e
else:
    result=r.json()
    print(type(result),result)

proxies={
    "http":"http://10.10.1.10:3128",
    "https":"http://10.10.1.10:1080",
}
r=requests.get("http://www.zhidaow.com",proxies=proxies)
print  r.request.headers
print r.text