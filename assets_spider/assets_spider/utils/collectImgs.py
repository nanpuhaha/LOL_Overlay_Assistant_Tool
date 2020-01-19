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


if __name__ == '__main__':
    ts = calendar.timegm(time.gmtime())
    # load csv file
    df = pd.read_csv('../results/champion.csv', delimiter=',')
    nameList = tuple(df['cn_name'])
    banner_pic_urls = df['banner_pic_url'].tolist()
    detail_pic_urls = df['detail_pic_url'].tolist()
    list_pic_urls = df['list_pic_url'].tolist()
    # traverse all img url and download
    for name, banner_url, detail_url, list_url in zip(nameList, banner_pic_urls, detail_pic_urls, list_pic_urls):
        path = "./triple/" + name
        if not os.path.exists(path):
            os.mkdir(path)
        download(path, banner_url, "banner")
        download(path, detail_url, "detail")
        download(path, list_url, "list")
