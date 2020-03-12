import datetime
import time


def date2str(date, date_format="%Y%m%d%H%M%S"):
    str = date.strftime(date_format)
    return str


print(date2str(20191600000080))
