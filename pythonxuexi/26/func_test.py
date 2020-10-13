import time
# 闭包函数


def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("运行时间是 %s 秒" % (end_time - start_time))
    return wrapper()

# 装饰器函数


@timmer
def i_can_sleep():
    time.sleep(3)


i_can_sleep
