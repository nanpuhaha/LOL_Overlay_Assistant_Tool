# -*- coding: utf-8 -*-
import scrapy
from assets_spider.items import ItemItem


def wrapURL(url):
    if url.startswith("//"):
        return f"http:{url}"


def wrapName(name):
    return name.replace(' ', '_').lower()


class TFTCardSpiderSpider(scrapy.Spider):
    name = 'tft_card_spider'
    allowed_domains = ['101.qq.com']
    start_urls = ['http://101.qq.com/tft/?ADTAG=cooperation.glzx.tft']

    def parse(self, response):
        cost1Img = response.xpath("//div[@class='champion-list body clearfix show']//div[@class='champion cost1']//img/@src")
        for img in cost1Img:
            print(img.root)
        # nameList = response.xpath("//div[@class='tab-content position-relative']//img/@alt")
        # for url, name in set(zip(imgURLList, nameList)):
        #     item = ItemItem()
        #     item['name'] = wrapName(name.root)
        #     item['imgUrl'] = wrapURL(url.root)
        #     yield item
