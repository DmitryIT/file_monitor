import os
from datetime import datetime, timedelta
from time import sleep

PATH = "/Users/dmitry/PycharmProjects/sandbox/file_monitor/"
NAME = "test.log"

MAX_DELTA = timedelta(minutes=1)

fd = PATH + NAME
while True:
    statinfo = os.stat(fd)

    now = datetime.now()
    mtime = datetime.fromtimestamp(statinfo.st_mtime)
    delta = now - mtime

    if delta > MAX_DELTA:
        print(fd + " is outdated")
        print("mtime = " + str(mtime))
        print("now =   " + str(now))
        break

    sleep(15)

