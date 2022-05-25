import requests  # 导入网络请求模块requests

"""
有无headers的区别
"""
if __name__ == '__main__':
    url = 'https://www.baidu.com/'  # 创建需要爬取网页的地址
    # 创建头部信息
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0)'
                             'Gecko / 20100101 Firefox / 72.0'}
    response = requests.get(url, headers=headers)  # 发送网络请求
    response2 = requests.get(url)  # 发送网络请求

    print(response2.encoding)
    print(response2.status_code)  # 打印响应状态码
    print(response2.text)

    print(response.encoding)
    print(response.status_code)  # 打印响应状态码
    print(response.text)
