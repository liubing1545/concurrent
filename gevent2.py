from gevent import monkey; monkey.patch_all()
import gevent
import requests

def f(url):
	print('GET: %s' % url)
	headers = {'User-Agent': 'Mozilla/5.0'}
	r = requests.get(url, headers = headers)
	print('%d bytes received from %s.' % (r.status_code, url))
 

gevent.joinall([
	gevent.spawn(f, 'https://www.baidu.com'), 
	gevent.spawn(f, 'https://www.sina.com'),
	gevent.spawn(f, 'http://www.douban.com')
])
