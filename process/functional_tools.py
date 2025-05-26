# process/functional_tools.py
from functools import reduce

def filter_low_quality(data):
    return list(filter(lambda d: d['sleep_quality'] < 50, data))

def average_deep_sleep(data):
    return reduce(lambda acc, d: acc + d['deep_pct'], data, 0) / len(data)
