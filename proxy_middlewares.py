import base64

# 代理服务器
proxyServer = "http://http-dyn.abuyun.com:9020"

# 代理隧道验证信息
proxyUser = "HH59908195O5720D"
proxyPass = "4B4748D2DBD1B53D"

# for Python3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        print('ProxyMiddleware......')
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth
