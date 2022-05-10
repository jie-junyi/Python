import urllib.request
import urllib.parse

if __name__ == '__main__':
    url = 'https://www.baidu.com/'  # 请求地址
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                             '(KHTML,like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
    data = bytes(urllib.parse.urlencode({'hello': 'python'}), encoding='utf-8')
    r = urllib.request.Request(url=url, headers=headers, data=data)
    response = urllib.request.urlopen(r)
    print(response.read().decode('utf-8'))
