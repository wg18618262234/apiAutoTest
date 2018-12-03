from common import request, excelaction

postdata = {}
headers = {'Host': 'test1.unicompayment.com', 'Connection': 'keep-alive', 'Pragma': 'no-cache',
           'Cache-Control': 'no-cache', 'Accept': 'application/json', 'Origin': 'https://test1.unicompayment.com',
           'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
           'Referer': 'https://test1.unicompayment.com/wopay-jd2/order/homepage/homepage.do',
           'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.9',
           # 'Cookie': 'bizFrom=226; _fmdata=b0RvBHVGOEbKrxCNjg3NCEFV3jgoC5w9fNdysbuh3D8ZAWo3jsq9gnkICNlA%2B16cyTOmTSz5JRyhhzavQX8MQQqF0yFQV7JeqdzFelPuS%2Bw%3D; woauth_tgc=tgt-273c10469a6146b8af8590c3eec58812-int; WT_FPC=id=2661cd8eb7997f0a23a1542698492784:lv=1542698515328:ss=1542698492784; TOKENID_COOKIE=chinaunicom-46QOPF45M7TNEZ4ANXJP9MQYV44LMJTR',
           'Content-Length': '0', 'Content-Type': 'application/x-www-form-urlencoded'}

excel = excelaction.excel()
i = 1
while True:
    if excel.read_excel(i) == False:
        break
    data = excel.read_excel(i)
    url = str(data[2])
    urldata = data[5]
    print(excel.read_excel(i))
    i += 1

    a = request.Request_post_cookie(url=url, postdata=[], headers=headers, )
    a.Cookie_add()
    a.Request_urlopen_read()
    print(a.Get_html())
