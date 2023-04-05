from src import utils
from datetime import datetime


def test_gen():
    now = datetime.now()
    result = utils.day_time_generator()

    assert now.strftime("%y-%m-%d") == result
