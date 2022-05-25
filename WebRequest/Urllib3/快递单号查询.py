import urllib3
import urllib.parse
import json  # 解析获得的数据
import msvcrt  # getch()获取一个按键(键盘输入)响应并返回对应的字符

kd_dict = {1: 'shentong', 2: 'youzhengguonei', 3: 'yuantong', 4: 'shunfeng', 5: 'yunda', 6: 'zhongtong', 7: "tiantian",
           8: "debang"}


def Check():
    while True:
        print("仅支持以下快递公司查询:")
        print("1.申通    ")
        print("2.EMS邮政    ")
        print("3.圆通    ")
        print("4.顺风    ")
        print("5.韵达    ")
        print("6.中通    ")
        print("7.天天    ")
        print("8.德邦    ")
        print("0.退出\n")
        choose = int(input("请选择您的快递公司:"))
        while choose not in range(0, 7):
            choose = int(input("抱歉暂不支持此公司请重新选择:"))
        if choose == 0:
            print("感谢使用!\n")
            break
        kd_num = input("请输入快递单号:")
        params = {'type': kd_dict[choose], 'postid': kd_num}
        http = urllib3.PoolManager()
        #  https://www.kuaidi100.com/query?type=yuantong&postid=YT3194517474668&temp=0.4745323602262068&phone=
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'}
        base_url = "http://www.kuaidi100.com/query?"
        url = base_url + urllib.parse.urlencode(params)
        response = http.request("POST", url=url, headers=header)
        html = response.read().decode('utf-8')
        target = json.loads(html)
        # print(target)
        status = target['status']
        if status == '200':
            data = target['data']
            # print(data)
            data_len = len(data)
            # print(data_len)
            # print("\n")
            for i in range(data_len):
                print("\n时间: " + data[i]['time'])
                print("状态: " + data[i]['context'] + "")
            print("\n感谢使用!\n")
            break
        else:
            print("输入有误请重新输入!\n")
    # print("按任意键结束......")


if __name__ == '__main__':
    while True:
        Check()
        out = input("按任意数字退出(其他键继续).........")
        if out >= '0' and out <= '9':
            break
        else:
            print("\n")
            continue
