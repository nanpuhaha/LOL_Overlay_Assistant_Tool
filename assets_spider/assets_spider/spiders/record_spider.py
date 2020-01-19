# -*- coding: utf-8 -*-
import scrapy

class RecordSpiderSpider(scrapy.Spider):
    name = 'record_spider'
    allowed_domains = ['ossweb-img.qq.com']
    start_urls = ['http://apps.game.qq.com/daoju/go/zmgoods/list?cat=16&page=1&plat=android&version=9921']

    def parse(self, response):
        pass
