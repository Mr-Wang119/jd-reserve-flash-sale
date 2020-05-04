# -*- encoding=utf8 -*-
from jdEmail import sendMail


class message(object):
    """消息推送类"""

    def __init__(self, mail):
        if not mail:
            raise Exception('mail can not be empty')
        self.mail = mail

    def send(self, desp='', isOrder=False):
        desp = str(desp)
        if isOrder:
            msg = desp + ' 类型口罩，已经下单了。24小时内付款'
        else:
            msg = desp + ' 类型口罩，下单失败了，快去抢购！'
        sendMail(self.mail, msg)
