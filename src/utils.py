import os.path
from datetime import datetime
from os import listdir
from os.path import isfile, join


def get_files(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


def day_time_generator() -> str:
    """
    Generate string("%y-%m-%d") from datetime
    :return:
    """
    now = datetime.now()
    gen = now.strftime("%y-%m-%d")
    print(f"date time : {gen}")
    return gen


def create_folder(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError:
        pass
