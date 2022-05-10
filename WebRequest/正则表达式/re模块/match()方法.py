import re

"""
使用 match()方法匹配中国移动手机号码
"""


def matchMobile(mobile):
    pattren = r'(13[4-9]\d{8})$|(15[01289]\d{8})$'
    match = re.match(pattren, mobile)
    if match == None:
        print(mobile, ' 不是有效的中国移动手机号码。')
    else:
        print(mobile, ' 是有效的中国移动手机号码。')
        print(match)


if __name__ == '__main__':
    mobileList = ['13634228888', '13099887766', '15899897777', '15622889933']
    for mobile in mobileList:
        matchMobile(mobile)
