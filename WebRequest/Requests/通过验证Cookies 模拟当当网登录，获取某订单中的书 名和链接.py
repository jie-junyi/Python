import requests  # 导入网络请求模块
import re

if __name__ == '__main__':

    cookie = 'ddscreen=2; __permanent_id=20220525082859816290238572383840670; ' \
             '__visit_id=20220525082859842343147248055481378; __out_refer=; ' \
             'bind_cust_third_id=FAC39991804AC91FAEC5CFC33525C791; bind_custid=0; ' \
             'bind_union_id=UID_2C36C26A4342EEF5BF28C8CB980B39F2; tx_nickname=xP7PyMn6; ' \
             'tx_open_id=FAC39991804AC91FAEC5CFC33525C791; ' \
             'tx_figureurl=http://thirdqq.qlogo.cn/g?b=oidb&k=PZSiarDaoGbwicUMO04WGzuw&s=640&t=1651674419; ' \
             'bind_mobile=17870263605; USERNUM=t8Wy61VE3ICvWrGZJ2zvng==; ' \
             'login.dangdang.com=.AYH=&.ASPXAUTH=zM5XzZ7XIjPCQk25k9bqdnY/ZgItBHOB8o4KALJ0470m9G2GRSs0ew==; ' \
             'MDD_channelId=70000; MDD_fromPlatform=307; producthistoryid=1900471202; ' \
             'dangdang.com=email=MTc4NzAyNjM2MDUyMzM1NUBkZG1vYmlscGhvbmVfX3VzZXIuY29t&nickname=xP7PyMn6&display_id' \
             '=1871760811356&customerid=l8vEgLb103zOqDhFjVifWA==&viptype=&show_name=178%2A%2A%2A%2A3605; ' \
             'ddoy=email=1787026360523355%40ddmobilphone__user.com&nickname=%C4%FE%CF%C8%C9%FA&validatedflag=0' \
             '&agree_date=1; sessionID=pc_d07156eb94468f61da60725610fcff7742aeda8e3e03143cf1bcdf230a6c1bb6; ' \
             'order_follow_source=-%7C-O-123%7C%2311%7C%23login_third_qq%7C%230%7C%23; ' \
             'MDD_custId=Ugupyi31irt2GUrvQc6AKQ%3D%3D; MDD_username=178****3605; cart_id=4000000007728631574; ' \
             'cart_items_count=1; LOGIN_TIME=1653439492123; ' \
             'deal_token=1836ba5e13834503929de58975557845b6901079f99e9f21aa1cdf5d66def21651b6ccba16bbac070f; ' \
             'pos_6_start=1653439736395; pos_6_end=1653439736405; ' \
             'dest_area=country_id%3D9000%26province_id%3D112%26city_id%3D0%26district_id%3D0%26town_id%3D0; ' \
             'pos_0_start=1653439979684; pos_0_end=1653439979694; pos_9_end=1653439979708; ' \
             '__rpm=...1653439977772%7Cs_112100.94003212839%2C94003212840.1.1653439981026; __ozlvd=1653439981; ' \
             '__trace_id=20220525085303708158420692275232064 '
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
        'Cookie': cookie
    }
    response = requests.get('http://myhome.dangdang.com/myFavorite',
                            headers=headers)
    if response.status_code == 200:  # 请求成功时
        html = response.text  # 解析html代码
    pattern = r'<td[\s]*class="tab_w1">.*</td>'
    patterns2 = r'<div[\s]*class="image">.*title="(.*)"[\s]*href="(.*)".*</div>'
    patterns = r'<a[\s]*title="([^>"]*)"[\s]*href="([^>"]*)".*>'

    product = re.findall(patterns, html)
    """for productStr in productList[1:]:
        productPattern = 'href="([^>"]*)"[\s]*target[\s]*="_blank"[\s]*title="([^>"]*)"'
    string = productStr.replace("'", "\"")
    productInfo = re.search(productPattern, string)"""
    print(product)
    print(html)
    """print('productName: ', productInfo.groups()[1], ' productLink: ',
          productInfo.groups()[0])"""
