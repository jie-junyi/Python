"""
使用urllib库抓取斗破苍穹小说目录和全文并存储 (IPO分析)
 输入I：https://www.doupo1234.com/doupocangqiong/
 输出O：爬取每章内容和标题，并以标题命名，存储到novel文件夹中
 使用的python库：urllib、re
 爬虫关键要素：url确定、设置请求头、获取与解析响应
"""
import urllib.request
import urllib.parse
import re


def PaQuDouPO(i):
    baseurl = 'https://www.doupo1234.com/doupocangqiong/'
    url = baseurl + f'{i}.html'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'}
    r = urllib.request.Request(url=url, headers=header, method='GET')
    requests = urllib.request.urlopen(r)
    print(requests.read().decode('utf-8'))


if __name__ == '__main__':
    PaQuDouPO(1)
    match = re.search(r'href="([^>"])*"')
