import urllib.request
import urllib.error

"""
  在URLError类中提供了一个reason属性，可以通过这个属性了解出现异常的错误原因。例如，这里向一个
  根本不存在网络地址发送请求，然后调用reason属性查看错误原因。
 HTTPError类是URLError类的子类，主要用于处理HTTP请求所出现的异常，该类有以下三个属性：
 code：返回 HTTP状态码。
 reason：返回错误原因。
 headers：返回请求头
"""
if __name__ == '__main__':
    # URLError
    """
    try:
        # 向不存在的网络地址发送请求
        response = urllib.request.urlopen('http://site2.rjkflm.com:666/123index.html')
    except urllib.error.URLError as error:
        print(error.reason)
    """
    # HTTPError
    """
    try:
        # 向不存在的网络地址发送请求
        response = urllib.request.urlopen('http://site2.rjkflm.com:666/123index.html')
        print(response.status)
    except urllib.error.HTTPError as error:
        print("状态码为：",error.code)
        print("异常信息为：",error.reason)
        print('请求头信息如下：\n', error.headers)
    """
    # 双重异常捕获
    try:
        # 向不存在的网络地址发送请求
        response = urllib.request.urlopen('http://site2.rjkflm.com:666/123index.html',timeout=0.1)
    except urllib.error.HTTPError as error:  # HTTPError捕获异常信息
        print('状态码为：', error.code)  # 打印状态码
        print('HTTPError异常信息为：', error.reason)  # 打印异常原因
        print('请求头信息如下：\n', error.headers)  # 打印请求头
    except urllib.error.URLError as error:  # URLError捕获异常信息
        print('URLError异常信息为：', error.reason)