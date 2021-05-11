from datetime import datetime
from collections import namedtuple
from math import floor

MS_PER_SECOND = 1000
MS_PER_MINUTE = MS_PER_SECOND * 60
MS_PER_HOUR = MS_PER_MINUTE * 60
MS_PER_DAY = MS_PER_HOUR * 24
MS_PER_WEEK = MS_PER_DAY * 7


Duration = namedtuple(
    'Duration', ['weeks', 'days', 'hours', 'minutes', 'seconds', 'ms'])


def ms_to_readable(ns: float) -> list[str]:

    weeks = floor(ns / MS_PER_WEEK)
    days = floor((ns % MS_PER_WEEK) / MS_PER_DAY)
    hours = floor((ns % MS_PER_DAY) / MS_PER_HOUR)
    minutes = floor((ns % MS_PER_HOUR) / MS_PER_MINUTE)
    seconds = floor((ns % MS_PER_MINUTE) / MS_PER_SECOND)
    ms = floor(ns % MS_PER_SECOND)

    return Duration(
        weeks,
        days,
        hours,
        minutes,
        seconds,
        ms
    )


def diff_datetimes(date_a: datetime, date_b: datetime) -> float:
    delta: float = abs(date_a.timestamp() - date_b.timestamp())
    return ms_to_readable(delta * 1000)


def diff_timestamp(unix_a: float, unix_b: float) -> float:
    delta: float = abs(unix_a - unix_b)
    return ms_to_readable(delta * 1000)
