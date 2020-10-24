#!/usr/bin/env python3

import datetime


class Logger(object):
    def __init__(self):
        pass

    def print(cls, msg):
        time_stamp = datetime.datetime.now()
        print("[%s]%s" % (time_stamp.strftime("%Y.%m.%d %H:%M:%S"), msg))
