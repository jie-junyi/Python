import re
"""
1:排除字符串的使用
2:分组group()和groups()的使用
  groups()---得到一个元组  ('//www.doupo1234.com/doupocangqiong/1.html', '第一章 陨落的天才')
  group()----返回字符串匹配结果  href="//www.doupo1234.com/doupocangqiong/1.html" title="第一章 陨落的天才"
  group(1)---返回元组的子分组  //www.doupo1234.com/doupocangqiong/1.html
"""

if __name__ == '__main__':
    str1 = '<li class="line3"><a href="//www.doupo1234.com/doupocangqiong/1.html" title="第一章 陨落的天才">第一章 陨落的天才</a></li>'
    partern1 = r'href="([^>"]*)"[\s]*title="([^>"]*)"'
    match = re.search(partern1, str1)
    match2 = re.search('href="([^>"]*)"[\s]*title="([^>"]*)"', str1)

    print(match.groups())
    print(match.group())
    print(match.group(0))
    print(match.group(1))

    print(match2)
