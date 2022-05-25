import urllib.request
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'}


# 不需要缓存东西，所以不需要在请求头中设置cookie

def getCatelogs(url):
    req = urllib.request.Request(url=url, headers=headers, method="GET")
    response = urllib.request.urlopen(req)
    result = []  # 提前声明好result是一个列表
    if response.status == 200 or response.status == 304:
        html = response.read().decode('utf-8')

        # 解码后的html是一个杂乱无章的东西，需要从这里面提取出所有格式如下的东西
        # 格式为 <li class="line3"><a href="//www.doupo1234.com/doupocangqiong/1.html" title="第一章 陨落的天才">第一章 陨落的天才</a></li>

        aList = re.findall('<li class="line3">.*</li>', html)
        print(len(aList))
        print(aList[0])
        for a in aList:
            match = re.search('href="([^>"]*)"[\s]*title="([^>"]*)"', a)

            # [^] ：除了这里面的符号，其他都可以匹配；如果遇到这里面的符号，就不再进行匹配，且最终结果不包括这个符号
            # eg：b='acbda"s'  match = re.search('[^"]*',b)  print(match.group())
            #  最终的结果为 acbda

            if match != None:
                url = "https:" + match.group(1)
                title = match.group(2)

                # 注意search与findall中的“（）”的含义是不一样的
                # findall中的“（）”表示的是分组，最终返回的只有括号里的内容
                # 而search与match中的“（）”，只有在.group（1）命令语句中才会返回正则表达式中第一个括号中匹配到的内容
                # 以此类推，.group（2）返回正则表达式中第二个括号匹配到的内容
                # 且.group()与.group(0)的运行结果相同

                chapter = {'title': title, 'url': url}
                result.append(chapter)
    return result


def getChapterContent(chapters):
    "for chapter in chapters:"
    chapter = chapters[0]
    req = urllib.request.Request(url=chapter['url'], headers=headers, method='GET')
    response = urllib.request.urlopen(req)
    if response.status == 200:
        print("正在写入中...")
        f = open('novel/' + chapter['title'] + '.txt', 'w')

        # .*?是懒惰模式（？必须跟在*或者+后面使用）
        contents = re.findall('<p>(.*?)</p>', response.read().decode('utf-8'))
        # 根据《斗破苍穹》的源代码中，每一句话都是<p>(.*?)</p>的格式

        for content in contents:
            f.write(content + '\n')
        f.close()
        print(chapter['title'], chapter['url'])


if __name__ == "__main__":
    chapters = getCatelogs('https://www.doupo1234.com/doupocangqiong/')
    getChapterContent(chapters)
