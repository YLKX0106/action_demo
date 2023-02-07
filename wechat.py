import json

import requests


def send(title, con):
  get_token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww3f3ad847e1fd104d&corpsecret=nEx0mllUXTx7PU8mxOXiTW6pBgXPU1Gf2NB1KGMxueQ"

  res = requests.get(url=get_token_url)
  access = res.json()['access_token']

  url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + access

  send_content = {
    "safe": 0,
    "touser": "@all",
    "agentid": 1000003,
    "textcard": {
      "title": title,
      "description": con,
      "url": "URL",
      "btntxt": "更多"
    },
    "msgtype": "textcard"
  }
  send_msges = (bytes(json.dumps(send_content), 'utf-8'))
  res = requests.post(url, send_msges)
