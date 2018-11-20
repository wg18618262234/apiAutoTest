from urllib import parse, request
from http import cookiejar


# post请求有cookie
class Request_post_cookie():
    def __init__(self, url, postdata=[], headers=[]):
        self.url = url
        self.data = parse.urlencode(postdata).encode('UTF8')
        self.headers = headers

    def Cookie_add(self):
        self.cookie = cookiejar.CookieJar()
        self.handlex = request.HTTPCookieProcessor(self.cookie)
        self.opener = request.build_opener(self.handlex)

    def Request_urlopen_read(self):
        print(self.url, self.data, self.headers)
        self.req = request.Request(url=self.url, data=self.data, headers=self.headers)
        self.response = self.opener.open(self.req)
        self.html = self.response.read()

    def Get_html(self):
        return self.html


# post请求无cookie
class Request_post():
    def __init__(self, url, postdata=[], headers=[]):
        self.url = url
        self.data = parse.urlencode(postdata).encode('UTF8')
        self.headers = headers

    def Request_urlopen_read(self):
        print(self.url, self.data, self.headers)
        self.req = request.Request(url=self.url, data=self.data, headers=self.headers)
        self.response = request.urlopen(self.req)
        self.html = self.response.read()

    def Get_html(self):
        return self.html


# get请求无cookie
class Request_get():
    def __init__(self, url, query_string, headers=[]):
        self.url = url + '?' + parse.urlencode(query_string).encode('UTF8')
        self.headers = headers

    def Request_urlopen_read(self):
        print(self.url, self.data, self.headers)
        self.req = request.Request(url=self.url, headers=self.headers)
        self.response = request.urlopen(self.req)
        self.html = self.response.read()

    def Get_html(self):
        return self.html


# get请求有cookie
class Request_get_cookie():
    def __init__(self, url, query_string, headers=[]):
        self.url = url + '?' + parse.urlencode(query_string).encode('UTF8')
        self.headers = headers

    def Cookie_add(self):
        self.cookie = cookiejar.CookieJar()
        self.handlex = request.HTTPCookieProcessor(self.cookie)
        self.opener = request.build_opener(self.handlex)

    def Request_urlopen_read(self):
        print(self.url, self.data, self.headers)
        self.req = request.Request(url=self.url, headers=self.headers)
        self.response = self.opener.open(self.req)
        self.html = self.response.read()

    def Get_html(self):
        return self.html


if __name__ == '__main__':
    url = 'https://test1.unicompayment.com/wopay-jd2/goodList/home/banner.do'
    postdata = {}
    headers = {'Host': 'test1.unicompayment.com', 'Connection': 'keep-alive', 'Pragma': 'no-cache',
               'Cache-Control': 'no-cache', 'Accept': 'application/json', 'Origin': 'https://test1.unicompayment.com',
               'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
               'Referer': 'https://test1.unicompayment.com/wopay-jd2/order/homepage/homepage.do',
               'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9',
               # 'Cookie': 'bizFrom=226; _fmdata=b0RvBHVGOEbKrxCNjg3NCEFV3jgoC5w9fNdysbuh3D8ZAWo3jsq9gnkICNlA%2B16cyTOmTSz5JRyhhzavQX8MQQqF0yFQV7JeqdzFelPuS%2Bw%3D; woauth_tgc=tgt-273c10469a6146b8af8590c3eec58812-int; WT_FPC=id=2661cd8eb7997f0a23a1542698492784:lv=1542698515328:ss=1542698492784; TOKENID_COOKIE=chinaunicom-46QOPF45M7TNEZ4ANXJP9MQYV44LMJTR',
               'Content-Length': '0', 'Content-Type': 'application/x-www-form-urlencoded'}
    # headers = {'cache-control': 'no-cache',
    #            'Postman-Token': '7d6c5fca-e342-402c-b69e-577b1ebc1084',
    #            'User-Agent': 'PostmanRuntime/7.3.0',
    #            'Accept': '*/*',
    #            'Host': 'test1.unicompayment.com',
    #            'accept-encoding': 'gzip, deflate',
    #            'Connection': 'close',
    #            'Content-Length': '0'}

    a = Request_post_cookie(url=url, postdata=[], headers=headers, )
    a.Cookie_add()
    a.Request_urlopen_read()
    print(a.Get_html())
