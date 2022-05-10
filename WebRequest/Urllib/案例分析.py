import urllib.request
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
        params = {'com': kd_dict[choose], 'nu': kd_num}

        #  https://www.kuaidi100.com/query?type=yuantong&postid=YT3194517474668&temp=0.4745323602262068&phone=
        header = {
            'Cookie':'BIDUPSID=057EBE4F72DAB2E307D91583F4B71210; PSTM=1642986409; __yjs_duid=1_a3df645423d9178c99d33b2c1407f9c51642989300609; BDUSS=FotWlBQRkJqN2c3U35aeHBxemZyWU9GcUppVFF2RVhvcy02UEhjZ3lLV0V6SkZpRVFBQUFBJCQAAAAAAAAAAAEAAADkwHhmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIQ~amKEP2piT; BDUSS_BFESS=FotWlBQRkJqN2c3U35aeHBxemZyWU9GcUppVFF2RVhvcy02UEhjZ3lLV0V6SkZpRVFBQUFBJCQAAAAAAAAAAAEAAADkwHhmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIQ~amKEP2piT; RT="z=1&dm=baidu.com&si=73sy7yg64ng&ss=l2l8fqmf&sl=6&tt=2e8&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=82q"; BAIDUID=56A10D8E583A25CEE08CAB01F43F2B2C:FG=1; BAIDUID_BFESS=56A10D8E583A25CE59F165B909CD956B:FG=1; BA_HECTOR=002g0l848k84a485rb1h73h590q; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=3; H_PS_PSSID=36184_36309_31254_34813_35911_36166_34584_35979_36342_36075_35864_26350_36348_36314_36061; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'}
        base_url = "https://express.baidu.com/express/api/express?query_from_srcid=4004&isBaiduBoxApp=10002&isWisePc=10020&tokenV2=phixpJB90MvfLYS0VwuMG9ELlVnfeOQpnJQf-pej2yoA7P1eIlrxIaSW0YnNrkJu&cb=jQuery110209152110234323174_1651623080574&appid=4001&"
        url = base_url + urllib.parse.urlencode(params)
        url2=url+'&vcode=&token=&qid=c4aa5c76002f9cc1&_=1651623080591'
        r = urllib.request.Request(url=url2, headers=header)
        response = urllib.request.urlopen(r)
        html = response.read().decode('utf-8')
        print(html)
        #target = json.loads(html)
        #print(target)
        '''
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
    '''


if __name__ == '__main__':
    while True:
        Check()
        out = input("按任意数字退出(其他键继续).........")
        if out >= '0' and out <= '9':
            break
        else:
            print("\n")
            continue
