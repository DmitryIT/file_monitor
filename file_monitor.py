#!/usr/local/bin/python3
import argparse
import os
from datetime import datetime, timedelta
from time import sleep

MAX_DELTA = timedelta(minutes=1)


def file_monitor():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="absolute path to file")
    args = parser.parse_args()

    fd = args.file
    # fd = os.path.join(PATH, NAME)

    if os.path.exists(fd):
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

            sleep(10)
    else:
        print("path " + fd + " doesn't exist")


if __name__ == "__main__":
    file_monitor()