import socket
import urllib.request
import urllib.error
import urllib.parse

if __name__ == '__main__':
    # 返回"http.client.HTTPResponse”对象。
    try:
        data = bytes(urllib.parse.urlencode({'hello': 'python'}), encoding='utf-8')
        response = urllib.request.urlopen(url='https://www.baidu.com/', data=data, timeout=1)
        # 读取全部的
        print(response.read().decode('utf-8'))
    except urllib.error.URLError as error:
        if isinstance(error.reason, socket.timeout):  # 判断异常是否为超时异常
            print('当前任务已超时，即将执行下一任务！')
            print(error.reason)
            print(socket.timeout)
