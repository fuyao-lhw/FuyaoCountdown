"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/9/15 23:58
@Project_Name   :  FuyaoCountdown
@Author         :  lhw
@File_Name      :  test.py

功能描述

实现步骤

"""
import datetime

from FuyaoCountdown.countdown import Countdown


def job():
    print("job is running")


if __name__ == '__main__':
    cd = Countdown(datetime.datetime.now().date(), 11, 51)

    cd.threadExecutor(True, job)
