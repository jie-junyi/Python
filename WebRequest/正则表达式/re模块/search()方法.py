import re

"""
使用 search()方法验证是否出现“危险”字符
"""


def dangerFilter(string):
    pattern = r'(黑客)|(抓包)|(监听)|(Trojan)'
    match = re.search(pattern, string)
    if match == None:
        print(string, ' @ 安全！')
    else:
        print(string, ' @ 出现了危险词汇！')


if __name__ == '__main__':
    strList = ['我是一名程序员，喜欢看黑客方面的书，想研究一下Trojan。',
               '我是一名程序员，喜欢看python数据分析方面的书，喜欢爬虫。']
    for string in strList:
        dangerFilter(string)
