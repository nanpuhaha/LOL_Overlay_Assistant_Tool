# -*- coding: utf-8 -*-
import scrapy
from assets_spider.items import ItemItem


def wrapURL(url):
    if url.startswith("//"):
        return "http:" + url


def wrapName(name):
    return name.replace(' ', '_').lower()


class ItemSpiderSpider(scrapy.Spider):
    name = 'item_spider'
    allowed_domains = ['lolchess.gg/items']
    start_urls = ['https://lolchess.gg/items']

    def parse(self, response):
        imgURLList = response.xpath(
            "//div[@class='tab-content position-relative']//img/@src")
        nameList = response.xpath("//div[@class='tab-content position-relative']//img/@alt")
        for url, name in set(zip(imgURLList, nameList)):
            item = ItemItem()
            item['name'] = wrapName(name.root)
            item['imgUrl'] = wrapURL(url.root)
            yield item
