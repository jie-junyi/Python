import urllib.parse

if __name__ == '__main__':
    # urlencode()方法对字典进行编码
    base_url = 'http://httpbin.org/get?'  # 定义基础链接
    params = {'name': 'Jack', 'country': '中国', 'age': 30}  # 定义字典类型的请求参数
    url = base_url + urllib.parse.urlencode(params)  # 连接请求地址
    print('编码后的请求地址为：', url)

    # quote()方法 对字符串进行编码
    base_url = 'http://httpbin.org/get?country='  # 定义基础链接
    url = base_url + urllib.parse.quote('中国')  # 字符串编码
    print('编码后的请求地址为：', url)

    # un......解码
    u = urllib.parse.urlencode({'country': '中国'})  # 使用urlencode编码
    q = urllib.parse.quote('country=中国')  # 使用quote编码
    print('urlencode编码后结果为：', u)
    print('quote编码后结果为：', q)
    print('对urlencode解码：', urllib.parse.unquote(u))
    print('对quote解码：', urllib.parse.unquote(q))

    # 使用 parse_qs()方法将参数转换为字典类型
    url = 'http://httpbin.org/get?name=Jack&country=%E4%B8%AD%E5%9B%BD&age=30'
    q = urllib.parse.urlsplit(url).query  # 获取需要的参数
    q_dict = urllib.parse.parse_qs(q)  # 将参数转换为字典类型的数据
    print('数据类型为：', type(q_dict))
    print('转换后的数据：', q_dict)

