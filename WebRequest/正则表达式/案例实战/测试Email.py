import re

"""
    测试Email
   输入：字符串列表，strList = ['lining@geekori.com', 'abcedfg@aa', '我的邮箱是jfzeng@ccnu.edu.cn，不是
bill@ieee.cn，请确认输入的Email是否正确！']
   输出：匹配每个字符串中的邮箱email，并输出格式为：str的匹配结果为：['lining@geekori.com']

"""
if __name__ == '__main__':
    strList = 'lining@geekori.com abcedfg@aa 我的邮箱是jfzeng@ccnu.edu.cn，不是bill@ieee.cn，请确认输入的Email是否正确！'
    ptn1 = r'.*com'
    #  比上面的难搞一点点
    ptn2 = r'[a-z@\.]*cn'
    matchList1 = re.findall(ptn1, strList, re.I)
    matchList2 = re.findall(ptn2, strList, re.I)

    print(matchList1)
    print(matchList2)
