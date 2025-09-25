# Countdown
python第三方库，实现到达目标时间执行函数

# 安装
``pip isntall FuyaoCountdown``

# 使用
```python
from FuyaoCountdown.countdown import Countdown
import datetime

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

    # cd.mainExecutor(job)

    cd.threadExecutor([job], [(1,)])


```

## 参数说明
```text

Countdown(
    date: str 日期,如 "2025-09-16",
    hour: int 小时,如 5
    minute: int 分钟,如 20
    second: int 秒,如 0
    nextTime: bool 当前目标时间到达后是否继续进行倒计时任务(明天的目标时间)
    threadPoolSize: int 线程池大小
)

# 线程池执行
Countdown.threadExecutor(
    job: list[Callable[..., Any]]  可调用的任意对象/函数(任务对象)
    jobArgs: list[tuple]  任务对象所需的参数
)

# 主线程执行--阻塞线程
Countdown.mainExecutor(
    job: Callable[..., Any]  可调用的任意对象/函数(任务对象)
    jobArgs: tuple  任务对象所需的参数
)

```


# 项目结构
```text
Countdown  项目名
    src  源代码
        FuyaoCountdown  软件包
    pyproject.toml  打包信息
    README.md  说明文件
    


```


# 更新日志

## v0.0.3
修复bug：


更新：

1.新增线程池配置

## v0.0.2
修复bug：

1.修复函数传参少的问题

2.修复传入datetime.date类型数据无法解析的问题


更新：

1.添加对执行到下一个目标时间的可选参数

2.增加日志记录,自动记录日志到调用文件的同级目录下

## v0.0.1
1.支持新线程执行任务