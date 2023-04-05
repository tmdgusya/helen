from datetime import datetime


def day_time_generator() -> str:
    """
    Generate string("%y-%m-%d") from datetime
    :return:
    """
    now = datetime.now()
    gen = now.strftime("%y-%m-%d")
    print(f"date time : {gen}")
    return gen
