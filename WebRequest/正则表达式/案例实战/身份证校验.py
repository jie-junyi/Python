import re

"""
    身份证校验
   输入：身份证字符串列表，ID_list = ['42010619700915553x', '42010219671231204x', '420106196704263212']
    
"""
if __name__ == '__main__':
    ID_list = ['42010619700915553x', '42010219671231204x', '420106196704263212']
    ptn = r'((42010\d)((19|20)(?:\d{2}))(\d{2})(\d{2})(\d{2})(\d).)'
    for i in ID_list:
        matchList = re.findall(ptn, i, re.I)
        matchyuanzu=matchList[0]
        inn = int(matchyuanzu[7])
        if (inn % 2 == 0):
            str1 = '女'
        else:
            str1 = '男'

        print(f'ID: {matchyuanzu[0]}  birthday: {matchyuanzu[2]}-{matchyuanzu[3]}-{matchyuanzu[4]}'
              f' sex: {str1}')
