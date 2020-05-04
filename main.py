#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant
from util import parse_time, parse_sku_id_to_list
import pdb
import threading
import time

from log import logger

'''
抢购线程
'''
class BuyProcess (threading.Thread):
    def __init__(self, threadID, skuid, buy_time, asst, num):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.skuid = skuid
        self.buy_time = buy_time
        self.asst = asst
        self.num = num
    def run(self):
        self.asst.exec_seckill_by_time(self.skuid, self.buy_time, num=self.num)

'''
预定线程
'''
class ReserveProcess (threading.Thread):
    def __init__(self, threadID, skuid, reserve_time, buy_time, asst):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.skuid = skuid
        self.reserve_time = reserve_time
        self.buy_time = buy_time
        self.asst = asst
    def run(self):
        self.asst.make_reserve_on_time(self.skuid, self.reserve_time)


if __name__ == '__main__':

    sku_ids = '65708238590,100011521400,65624145328,100006394713,100011551632'  # 商品id
    sku_nums = '1,1,1,1,1'
    all_reserve_time = '10:59:30.000,20:59:30.000,10:59:30.000,14:59:30.000,14:59:30.000'
    all_buy_time = '17:00:00.050,10:00:00.050,15:00:00.050,20:00:00.050,20:00:00.050'
    area = '6_303_36780_56047'  # 区域id
    max_reserve_threads_num = 6


    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆

    # 转list和dict
    sku_ids_list = parse_sku_id_to_list(sku_ids)
    reserve_time_list = parse_time(all_reserve_time)
    buy_time_list = parse_time(all_buy_time)

    i=0

    for (sku_id, reserve_time, buy_time, sku_num) in zip(sku_ids_list, reserve_time_list, buy_time_list, sku_nums):
        local_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
        if reserve_time[:len(local_time)]>local_time:
            cur_reserve_process = ReserveProcess(i, sku_id, reserve_time, buy_time, asst)
            cur_reserve_process.start()
            logger.info('%s 预约进程开启', sku_id)
            time.sleep(2)
        else:
            logger.info('%s 预约时间已过', sku_id)
            time.sleep(2)
        if buy_time[:len(local_time)]>local_time:
            cur_buy_process = BuyProcess(i+1, sku_id, buy_time, asst, sku_num)
            cur_buy_process.start()
            logger.info('%s 购买进程开启', sku_id)
            time.sleep(2)
        else:
            logger.info('%s 购买时间已过', sku_id)
            time.sleep(2)
        i += 2
