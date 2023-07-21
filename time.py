import time

def focus_clock(total_time, work_interval, rest_interval):
    """
    专注时钟函数

    参数：
    total_time: 总共的专注时间（以秒为单位）
    work_interval: 工作时间间隔（以秒为单位）
    rest_interval: 休息时间间隔（以秒为单位）
    """

    while total_time > 0:
        print(f"工作 {work_interval} 秒")
        time.sleep(work_interval)
        total_time -= work_interval

        if total_time <= 0:
            break

        print(f"休息 {rest_interval} 秒")
        time.sleep(rest_interval)
        total_time -= rest_interval

if __name__ == "__main__":
    total_time = 60 * 25  # 总共的专注时间：25分钟
    work_interval = 60 * 25  # 工作时间间隔：25分钟
    rest_interval = 60 * 5  # 休息时间间隔：5分钟

    focus_clock(total_time, work_interval, rest_interval)
