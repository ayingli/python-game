# -*- coding: utf-8 -*-
__author__ = 'ouyangmin'
__time__ = '2021/2/14 23:15'
# 如果该代码不能满足您日常工作需求，可发邮件到liyysap@126.com ，说清楚您的需求，我尽力帮您实现哦

from threading import Timer
from wxpy import *

bot = Bot()

def read_file():
    datas = []
    with open('love_yaya.csv', 'r', encoding='utf-8') as lines:
        for line in lines:
            datas.append(line)
    return datas

def send_massage(datas, i):
    try:
        end_massage = "永远爱你的狮子"
        # 获取好友备注
        my_friend = bot.friends().search(u'等等')[0]
        # 发送消息
        my_friend.send(datas[i])
        my_friend.send(end_massage)
        # 每86400秒（1天），发送1次
        i = i + 1
        item = (datas, i)
        t = Timer(86400, send_massage, item)
        t.start()
    except:
        my_friend = bot.friends().search(u'等等')[0]
        my_friend.send(datas[i])
        my_friend.send(u"今天消息发送失败了，狮子依然永远的爱你")

if __name__ == '__main__':
    datas = read_file()
    send_massage(datas, 0)

