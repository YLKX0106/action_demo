import re

import requests
from fake_useragent import UserAgent

import wechat


def sign():
    ua = UserAgent()
    headers = {
        'User-Agent': ua.chrome
    }

    url = 'https://paoluz.link/auth/login'
    data = {
        'email': 'qR3pMHHvf3Rf@126.com',
        'passwd': 'gTBLQ36M5aIWqnmA',
        'code': '',
        'remember_me': 'on'
    }

    global session
    session = requests.session()
    session.post(url=url, headers=headers, data=data)

    # 签到
    url = 'https://paoluz.link/user/checkin'

    res = session.post(url=url, headers=headers)
    msg = res.json()['msg']

    # 信息获取
    url = 'https://paoluz.link/user'
    res = session.get(url=url, headers=headers)
    # 剩余流量
    result = re.search(r'<span class="counter">(\d+\.\d+)</span>', res.text).group(1)
    # 天数
    result1 = re.search(r'<span class="counter">(\d+)</span> +天', res.text).group(1)
    con = '{}\n剩余流量:{}GB\n剩余时间:{}天'.format(msg, result, result1)
    wechat.send('机场签到(泡泡云)', con)


if __name__ == '__main__':
    sign()
