import math
import urllib.request
import os
from urllib.error import HTTPError

import pandas as pd


def download(dir_name, url, name):
    try:
        rsp = urllib.request.urlopen(url)
        img = rsp.read()
        with open(dir_name + "/" + name + ".jpg", 'wb') as f:
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


if __name__ == '__main__':
    df = pd.read_csv('../results/tft_10.1_champ.csv', delimiter=',')
    nameList = df['cn_name'].tolist()
    urlList = df['card_img_url'].tolist()
    path = "./cards"

    for url, name in zip(urlList, nameList):
        if not os.path.exists(f"{path}/" + name):
            os.mkdir(f"{path}/" + name)
        if url not in [None, ""]:
            print("going to crawl url -> ", url)
            download2(f"{path}/" + name, url)
