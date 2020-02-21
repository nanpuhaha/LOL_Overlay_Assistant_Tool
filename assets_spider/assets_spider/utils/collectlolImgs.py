import calendar
import time
from urllib.error import HTTPError

import pandas as pd
import urllib.request
import os


def download(dir_name, url, type="banner"):
    try:
        rsp = urllib.request.urlopen(url + "?_t=" + str(calendar.timegm(time.gmtime())))
        img = rsp.read()
        with open(dir_name + "/" + type + ".jpg", 'wb') as f:
            f.write(img)
    except HTTPError:
        print("Oops!  Something Wrong Happened, check dir -> ", dir_name)


def download2(dir_name, url):
    try:
        rsp = urllib.request.urlopen(url)
        img = rsp.read()
        with open(dir_name + "/card.jpg", 'wb') as f:
            f.write(img)
    except HTTPError:
        print("Oops!  Something Wrong Happened, check dir -> ", dir_name)


def download3(dir_name, url, name):
    try:
        rsp = urllib.request.urlopen(url)
        img = rsp.read()
        with open(dir_name + "/" + name + ".jpg", 'wb') as f:
            f.write(img)
    except HTTPError:
        print("Oops!  Something Wrong Happened, check dir -> ", dir_name)


if __name__ == '__main__':
    # load csv file
    df = pd.read_csv('./ff.csv', delimiter=',')
    nameList = tuple(df['en_name'])
    pic_urls = df['url'].tolist()
    # traverse all img url and download
    for name, url in zip(nameList, pic_urls):
        path = "./avatar_en_temp/"
        if not os.path.exists(path):
            os.mkdir(path)
        download3(path, url, name)
