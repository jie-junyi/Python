import socket
import urllib.request
import urllib.error
import urllib.parse

if __name__ == '__main__':
    url = 'https://passport.mingrisoft.com/Login/checkLogin'  # 登录请求地址
    data = bytes(urllib.parse.urlencode({'username': 'zjfmrkj', 'password': 'zjfmrkj2020'}), encoding='utf-8')
    # 创建Request对象
    r = urllib.request.Request(url=url, data=data, method='POST')
    response = urllib.request.urlopen(r)
    print('响应状态码为: ', response.status)
    # 为什么拉不到信息？？？？
    print(response.read().decode('utf-8'))  # 读取HTML代码并进行
