import urllib.request
import urllib.parse

"""
       失败
"""
if __name__ == '__main__':
    url = 'https://www.httpbin.org/get'  # 网络请求地址
    # 创建代理IP
    proxy_handler = urllib.request.ProxyHandler({
        'https': '58.220.95.114:10053'
    })
    # 创建opener对象
    opener = urllib.request.build_opener(proxy_handler)
    response = opener.open(url, timeout=0.5)
    print(response.read().decode('utf-8'))
