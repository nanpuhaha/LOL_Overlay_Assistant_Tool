# -*- coding: utf-8 -*-

import requests
import re
import os

'''
Citation:
https://blog.csdn.net/MarkAdc/article/details/99710763

Modified by Aaron 2020-01-17
'''


class SkinSpider:

    def __init__(self):

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        }

    def getResponse(self, url):

        try:
            response = requests.get(url, headers=self.headers)
            response.encoding = 'utf-8'
            assert response.status_code == 200
            return response
        except:
            return None

    def run(self):

        heroInfo_url = "http://lol.qq.com/biz/hero/champion.js"
        heroInfoText = self.getResponse(heroInfo_url).text

        hero_info_list = re.findall('"id":"(.*?)","key":"(.*?)","name":"(.*?)","title":"(.*?)",', heroInfoText)

        # 构造一下将要保存的本地路径
        path = "./heroSkin2/"
        for hero_info in hero_info_list:
            item = {
                "en_name": hero_info[0],
                "key": hero_info[1],
                "cn_title": hero_info[2].encode().decode("unicode-escape"),
            }

            item["cn_name"] = hero_info[3].encode().decode("unicode-escape")

            if not os.path.exists(path):
                os.mkdir(path)
            self.requestSkinURl(path, item["key"], item["en_name"])

    def requestSkinURl(self, path, key, cn_name):

        num = int(key) * 1000
        oneSkinImgurl = "https://game.gtimg.cn/images/lol/act/img/skin/big{}.jpg"
        for skinPage in range(1):
            imgUrl = oneSkinImgurl.format(num + skinPage)
            img_response = self.getResponse(imgUrl)
            if img_response is None:
                break
            self.downloadImg(path, img_response.content, skinPage, cn_name)

    def downloadImg(self, path, bResponse, skinPage, cn_name):
        dir_name = path
        try:
            path = f"{path}/{cn_name}" + ".jpg".format(skinPage)
            if os.path.exists(path):
                return
            with open(path, "wb") as f:
                f.write(bResponse)
        except:
            print("Oops!  Something Wrong Happened, check dir -> ", dir_name)


if __name__ == '__main__':
    skin_spider = SkinSpider()
    skin_spider.run()
