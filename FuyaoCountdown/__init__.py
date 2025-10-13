"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/9/15 23:58
@Project_Name   :  FuyaoCountdown
@Author         :  lhw
@File_Name      :  __init__.py.py

功能描述

实现步骤

"""
import logging
import sys
from pathlib import Path
import os
import FuyaoCountdown

__version__ = "v0.0.3"

# 获取用户执行的脚本路径（sys.argv[0] 是启动脚本的路径）
userScriptPath = sys.argv[0]

# 获取脚本所在目录（如果是交互式环境，fallback到当前工作目录）
if userScriptPath:
    callerDir = os.path.dirname(os.path.abspath(userScriptPath))
else:
    callerDir = os.getcwd()

callerDir = Path(callerDir)

# 配置文件路径
CONFIG_PATH = Path(FuyaoCountdown.__file__).parent / "resources" / "config" / "config.json"

LOG_FILE_PATH_KEY = "logFilePath"

LOG_FILE_PATH = Path(callerDir) / "countdown.log"
# logFilePath = readConfig(LOG_FILE_PATH_KEY)


# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S',  # 时间格式
#     handlers=[
#         logging.FileHandler(logFilePath, encoding="utf-8"),  # 保存到文件
#         logging.StreamHandler(),  # 输出到控制台
#     ]
# )
#
# logger = logging.getLogger()

