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

# from FuyaoCountdown.countdown import Countdown
from src.FuyaoCountdown.countdown import Countdown


def job(param=None):
    print(param)

    print(f"{param} job is running")
    return {
        "jobParam": param
    }


if __name__ == '__main__':
    now = datetime.datetime.now()
    second = now.second
    cd = Countdown(now.date(), now.hour, now.minute, second=second + 1, nextTime=False)

    cd.mainExecutor(job)

    # cd.threadExecutor([job], [(1,), (2,)])

    print(1)
