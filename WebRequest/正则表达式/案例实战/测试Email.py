import re

"""
    测试Email
   输入：字符串列表，strList = ['lining@geekori.com', 'abcedfg@aa', '我的邮箱是jfzeng@ccnu.edu.cn，不是
bill@ieee.cn，请确认输入的Email是否正确！']
   输出：匹配每个字符串中的邮箱email，并输出格式为：str的匹配结果为：['lining@geekori.com']

"""


def EmailMatch(email):
    ptn3 = r'[a-z]*@[a-z.]*(?:cn|com)'
    matchList = re.findall(ptn3, email, re.I)
    print(email, " 的匹配结果为：", matchList)


if __name__ == '__main__':
    strList2 = ['lining@geekori.com', 'abcedfg@aa', '我的邮箱是jfzeng@ccnu.edu.cn，不是bill @ ieee.cn，请确认输入的Email是否正确！']
    for i in strList2:
        EmailMatch(i)
